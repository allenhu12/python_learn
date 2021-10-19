"""
name:           2019_tax.py
version:        1.0
description:    calculate the tax based on the 2019 new tax polices
"""

import math
#免征额
exemption=5000
#专项附加扣除
additional_deduct_collection={}
income_per_month_list=[0]
ratio_year_index=''
ratio_month_index='' 

tax_ratio_dict_year = {'less_60000':[0.03,0],
                  'large_60000_less_144000':[0.1,2520],
                  'large_144000_less_300000':[0.2,16920],
                  'large_300000_less_420000':[0.25,31920],
                  'large_420000_less_660000':[0.3,52920],
                  'large_660000_less_960000':[0.35,85920],
                  'large_960000':[0.45,181920]}

tax_ratio_dict_month = {'less_5000':[0.03,0],
                  'large_5000_less_12000':[0.1,210],
                  'large_12000_less_25000':[0.2,1410],
                  'large_25000_less_35000':[0.25,2660],
                  'large_35000_less_55000':[0.3,4410],
                  'large_55000_less_80000':[0.35,7160],
                  'large_80000':[0.45,15160]}
def main():
    i = 1
    while i < 13:
        income_per_month_list.append(15000)
        i += 1
    #income_per_month_list[12] = 50000
    tax_per_month_old = 0
    tax_per_month_new = 0
    tax_per_month_list_old = [0]
    tax_per_month_list_new = [0]
    i = 1
    while i < 13:
        tax_per_month_old = tax_calculate_per_month_old(i,income_per_month_list,5000,4000)
        tax_per_month_new = tax_calculate_per_month_new(i,income_per_month_list,5000,4000,tax_per_month_list_new)
        tax_per_month_list_old.append(tax_per_month_old)
        tax_per_month_list_new.append(tax_per_month_new)
        i += 1
        print("\n")

    print("Old tax per month:")
    print(tax_per_month_list_old)
    print("Old tax total per year:")
    print(math.fsum(tax_per_month_list_old))


    print("new tax per month:")
    print(tax_per_month_list_new)
    print("new tax total per year:")
    print(math.fsum(tax_per_month_list_new))


def tax_calculate_per_month_old(month_index, income_per_month_list, exemption, additional_deduct_per_month):
    income_this_month = income_per_month_list[month_index] - exemption - additional_deduct_per_month
    if income_this_month <= 5000:
        ratio_month_index = 'less_5000'
    elif income_this_month > 5000 and income_this_month <= 12000:
        ratio_month_index = 'large_5000_less_12000'
    elif income_this_month > 12000 and income_this_month <= 25000:
        ratio_month_index = 'large_12000_less_25000'
    elif income_this_month > 25000 and income_this_month <= 35000:
        ratio_month_index = 'large_25000_less_35000'
    elif income_this_month > 35000 and income_this_month <= 55000:
        ratio_month_index = 'large_35000_less_55000'
    elif income_this_month > 55000 and income_this_month <= 80000:
        ratio_month_index = 'large_55000_less_80000'
    else:
        ratio_month_index = 'large_80000'

    ls = tax_ratio_dict_month[ratio_month_index]
    # 该月应缴纳个税 = 该月实际应税收入 * 税率 - 速算扣除数 
    tax_this_month = income_this_month * ls[0] - ls[1]
    print("Month:{},Month income:{},Month income before tax:{},tax ratio:{},tax deduction:{},tax:{:.2f}".format\
              (month_index,income_per_month_list[month_index],income_this_month,ls[0],ls[1],tax_this_month))
    return tax_this_month


def tax_calculate_per_month_new(month_index, income_per_month_list, exemption, additional_deduct_per_month, tax_per_month_list_new ):
    """
    应纳税 = (税前收入 - 三险一金 - 免征额 - 依法确定的其他扣除 - 专项附加扣除) * 适用税率 - 速算扣除数   
    专项附加扣除:
	1   子女教育专项附加		每个子女(三岁到博士生期间)每月1000
	2   继续教育专项附加		每年3600或4800
	3   住房贷款利息专项  	        每月1000
	4   住房租金专项     	        每月800-1200
	5   赡养老人专项		每月2000
    """
    total_income_untill_this_month = 0
    i = 1
    while i <= month_index:
        total_income_untill_this_month += income_per_month_list[i]
        i += 1
    # 该月应缴纳税费都是使用到这个月为止的收入总额 - 专项扣除总额 - 额外专项扣除总额，所以需要*month_index
    income_to_calc_tax = total_income_untill_this_month - exemption*month_index - additional_deduct_per_month*month_index
    if income_to_calc_tax <= 60000:
        ratio_year_index = 'less_60000'
    elif income_to_calc_tax > 60000 and income_to_calc_tax <= 144000:
        ratio_year_index = 'large_60000_less_144000'
    elif income_to_calc_tax > 144000 and income_to_calc_tax <= 300000:
        ratio_year_index = 'large_144000_less_300000'
    elif income_to_calc_tax > 300000 and income_to_calc_tax <= 420000:
        ratio_year_index = 'large_300000_less_420000'
    elif income_to_calc_tax > 420000 and income_to_calc_tax <= 660000:
        ratio_year_index = 'large_420000_less_660000'
    elif income_to_calc_tax > 660000 and income_to_calc_tax <= 960000:
        ratio_year_index = 'large_660000_less_960000'
    else:
        ratio_year_index = 'large_960000'
    tax_already_sumbit = 0
    ls = tax_ratio_dict_year[ratio_year_index]
    if month_index == 1:
        tax = income_to_calc_tax * ls[0] - ls[1]
    else:
        tax_already_sumbit = math.fsum(tax_per_month_list_new)
        # 该月应缴纳个税 = 到该月为止实际应税收入总额 * 对应税率 - 对应速算扣除数 - 到该月为止已经缴纳的税费
        tax = income_to_calc_tax * ls[0] - ls[1] - tax_already_sumbit
    print("Month:{},total income:{},total income before tax:{},tax ratio:{},tax deduction:{},tax:{:.2f},tax_already_submit:{:.2f}".format\
              (month_index,total_income_untill_this_month,income_to_calc_tax,ls[0],ls[1],tax, tax_already_sumbit))
    return tax 

if __name__ == "__main__":
    main()

