"""
name:           2019_tax.py
version:        1.0
description:    calculate the tax based on the 2019 new tax polices
"""

#免征额
exemption=5000
#专项附加扣除
additional_deduct_collection={}
index = 0
tax_ratio_dict = {'less_36000':[0.03,0],
                  'large_36000_less_144000':[0.1,2520],
                  'large_144000_less_300000':[0.2,16920],
                  'large_300000_less_420000':[0.25,31920],
                  'large_420000_less_660000':[0.3,52920],
                  'large_660000_less_960000':[0.35,85920],
                  'large_960000':[0.45,181920]}

tax_ratio_dict1 = {'less_5000':[0.03,0],
                  'large_5000_less_12000':[0.1,210],
                  'large_12000_less_25000':[0.2,1410],
                  'large_25000_less_35000':[0.25,2660],
                  'large_35000_less_55000':[0.3,4410],
                  'large_55000_less_80000':[0.35,7160],
                  'large_80000':[0.45,15160]}
def main():
    tax_calculate(9000,2000)



def tax_calculate(income_before_tax_per_month,additional_deduct_per_month):
    """
    应纳税 = (税前收入 - 三险一金 - 免征额 - 依法确定的其他扣除 - 专项附加扣除) * 适用税率 - 速算扣除数   
    专项附加扣除:
	1   子女教育专项附加		每个子女(三岁到博士生期间)每月1000
	2   继续教育专项附加		每年3600或4800
	3   住房贷款利息专项  	        每月1000
	4   住房租金专项     	        每月800-1200
	5   赡养老人专项		每月2000
    """
    income_to_calc_tax = income_before_tax_per_month*12 - exemption*12 - additional_deduct_per_month*12
    print("The income to calculate the tax per year is {:.2f}".format(income_to_calc_tax));
    if income_to_calc_tax <= 36000:
        index = 'less_36000'
    elif income_to_calc_tax>36000 and income_to_calc_tax <= 144000:
        index = 'large_36000_less_144000'
    elif income_to_calc_tax > 144000 and income_to_calc_tax <= 300000:
        index = 'large_144000_less_300000'
    elif income_to_calc_tax > 300000 and income_to_calc_tax <= 420000:
        index = 'large_300000_less_420000'
    elif income_to_calc_tax > 420000 and income_to_calc_tax <= 660000:
        index = 'large_420000_less_660000'
    elif income_to_calc_tax > 660000 and income_to_calc_tax <= 960000:
        index = 'large_660000_less_960000'
    else:
        index = 'large_960000'
    ls = tax_ratio_dict[index]
    print("the ratio is {}, the deducting number is {}".format(ls[0],ls[1]))
    tax = income_to_calc_tax * ls[0] - ls[1]
    print("the tax per year is {:.2f}, the tax per month is {:.2f}".format(tax, tax/12))

    

if __name__ == "__main__":
    main()

