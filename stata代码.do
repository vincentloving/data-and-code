***熵值法计算绿色发展指数

********************定义求熵值程序********************
capture program drop shangzhi
program shangzhi
args var statue rn //var：待处理的变量statue=1表示正向指标,statue=-1表示负向指标, rn:r年与n个观测值的乘积
quietly{
*step1 归一化 `var'_sd
sum `var' 
scalar min=r(min)
scalar max=r(max)

g `var'_sd=(`var'-min)/(max-min)
if `statue'==-1{
noisily dis as error "负向指标"
replace `var'_sd=1-`var'_sd
}

*step2 计算占比 `var'_sdw
g  `var'_sds= `var'_sd+0.00000001 //注：添加偏移量0.00000001,可自行修改
egen `var'_sds_sum=sum(`var'_sds) //计算`var'_sds的总和
g  `var'_sdw=`var'_sds / `var'_sds_sum //计算`var'_sds的占比

*step3 计算熵值 `var'_s
g `var'_sij=-1*`var'_sdw*ln(`var'_sdw)/ln(`rn') //`var'_sij
egen `var'_s=sum(`var'_sij) //熵值`var'_s

*step4 计算信息效用 `var'_g
g `var'_g=1-`var'_s

*step5 清除多余变量:只保留`var'_sd，`var'_g
drop `var'_sds `var'_sdw `var'_sds_sum `var'_sij `var'_s 
}
end
***********************************

*****************主程序*************

*【1】求`var'_g
/*调用shangzhi程序，依次输入三个参数，
要处理的变量var,正向指标或者负向指标（1 or -1），r*n的数值（本文：10*30=300,10年，30个省市）
注：负向指标会提示文字，正向则不会*/

*注，以下代码可按需要修改
gen v1=二氧化碳排放量
gen v2=GTFP
gen v3=RD
gen v4=绿色产业占比/100
gen v5=绿色能源占比
gen v6=绿色专利占比
gen v7=废物利用率
*负向指标
shangzhi v1 -1 300

*正向指标
shangzhi v2 1 300
shangzhi v3 1 300
shangzhi v4 1 300
shangzhi v5 1 300
shangzhi v6 1 300
shangzhi v7 1 300
*【2】求权重wi
g sum_g=v1_g+v2_g+v3_g+v4_g+v5_g+v6_g ///
+v7_g

forvalues i=1/7{
g w`i'=v`i'_g/sum_g
}
drop sum_g 
list w* in 1 //展示权重

*【3】求最终得分hij
g h=v1_sd*w1+v2_sd*w2+v3_sd*w3+ ///
       v4_sd*w4+v5_sd*w5+v6_sd*w6+ ///
	   v7_sd*w7
drop *_*	   
*********************************************
rename h gdev

encode 省份,gen(province)
xtset province 年份
gen lnpgdp=log(人均GDP)
gen dige=数字经济指数
gen sdige=数字经济指数^2
gen urban=城镇化/100
gen lnft=log(进出口贸易)
gen lnhc=log(hc)

*基准回归,双固定
reg gdev dige
est store r1

xi:reg gdev i.年份 i.province dige sdige
est store r2

xi:reg gdev i.年份 i.province dige sdige lnpgdp
est store r3

xi:reg gdev i.年份 i.province dige sdige lnpgdp urban
est store r4

xi:reg gdev i.年份 i.province dige sdige lnpgdp urban lnft
est store r5

xi:reg gdev i.年份 i.province dige sdige lnpgdp urban lnft lnhc
est store r6
#输出结果
esttab r1 r2 r3 r4 r5 r6,scalar(N r2_a) star(* 0.1 ** 0.05 *** 0.01) b(%6.3f) t(%6.4f) indicate("年份 fe=_I年份*""province fe=_Iprovince*") nogap
esttab r1 r2 r3 r4 r5 r6 using jzbg.rtf,replace star(* 0.1 ** 0.05 *** 0.01) b(%6.3f) r2 se



***稳健性检验
*工具变量法
xi:reg 绿色能源占比 i.年份 i.province dige sdige lnpgdp urban lnft lnhc
est store r7

*差分GMM
xtabond2 gdev l1.gdev l2.gdev dige l1.dige sdige sldige  urban l1.urban lnpgdp l.lnpgdp lnft l1.lnft lnhc l1.lnhc i.年份 i.province,gmm(l1.gdev l1.dige sldige l1.urban l1.lnpgdp) iv(l2.gdev dige sdige urban lnpgdp lnft l1.lnft lnhc l1.lnhc i.年份 i.province) nolevel robust small
est store r8

*系统GMM
xtabond2 gdev l1.gdev l2.gdev dige l1.dige sdige sldige  urban l1.urban lnpgdp l.lnpgdp lnft l1.lnft lnhc l1.lnhc i.年份 i.province,gmm(l1.gdev l1.dige sldige l1.urban l1.lnpgdp) iv(i.年份 i.province) robust small
est store r9

*滞后一期解释变量
xi:reg gdev i.年份 i.province l.dige sldige lnpgdp urban lnft lnhc
est store r10

esttab r7 r8 r9 r10,scalar(N r2_a) star(* 0.1 ** 0.05 *** 0.01) b(%6.3f) t(%6.4f) indicate("年份 fe=_I年份*""province fe=_Iprovince*") nogap

esttab r7 r8 r9 r10 using wjx.rtf,replace star(* 0.1 ** 0.05 *** 0.01) b(%6.3f) r2 se


***数字经济门槛效应
set seed 80
xthreg gdev lnpgdp urban lnft lnhc nyear2 nyear3 nyear4 nyear5 nyear6 nyear7 nyear8 nyear9 nyear10, rx(dige) qx(dige) thnum(3) bs(1000 1000 1000) trim(0.05 0.05 0.05) grid(100) r
est store r11

*绘制单门槛图
xthreg gdev lnpgdp urban lnft lnhc nyear2 nyear3 nyear4 nyear5 nyear6 nyear7 nyear8 nyear9 nyear10, rx(dige) qx(dige) thnum(1) bs(2000) trim(0.01) grid(100) r
est store r12
_matplot e(LR), columns(1 2) yline(7.3523, lpattern(dash)) connect(direct) recast(line) ytitle("LR Statistics") xtitle("Dige") name(LR_dige)


***异质性

**数字经济
*高
xi:reg gdev i.年份 i.province dige sdige lnpgdp urban lnft lnhc
est store r13

*低
xi:reg gdev i.年份 i.province dige sdige lnpgdp urban lnft lnhc
est store r14

**绿色发展
*高
xi:reg gdev i.年份 i.province dige sdige lnpgdp urban lnft lnhc
est store r15

*低
xi:reg gdev i.年份 i.province dige sdige lnpgdp urban lnft lnhc
est store r16

**处罚
*多
xi:reg gdev i.年份 i.province dige sdige lnpgdp urban lnft lnhc
est store r17

*少
xi:reg gdev i.年份 i.province dige sdige lnpgdp urban lnft lnhc
est store r18

*支出
*多
xi:reg gdev i.年份 i.province dige sdige lnpgdp urban lnft lnhc
est store r19

*少
xi:reg gdev i.年份 i.province dige sdige lnpgdp urban lnft lnhc
est store r20


*输出结果
esttab r13 r14 r15 r16 r17 r18 r19 r20,scalar(N r2_a) star(* 0.1 ** 0.05 *** 0.01) b(%6.3f) t(%6.4f) indicate("年份 fe=_I年份*""province fe=_Iprovince*") nogap



