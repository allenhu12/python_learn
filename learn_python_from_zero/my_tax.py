#!/usr/bin/env python3
"""
version:            
name:               
functionality:
(1) will get the salary data online
(2) will get the tax based on the total salary and compare it with the online data
(3) will save the data into a excel file
"""

import math
# 字典赋值必须用深拷贝
import copy
#免征额
exemption=5000
#专项附加扣除, the data comes from published source
additional_deduct_collection={}
income_per_month_list=[0]
ratio_year_index=''
ratio_month_index=''
month_elderly_exemption = 2000
month_loan_exemption = 1000
# 广东全口径从业人员月平均工资
GD_AVERAGE_SALARY = 7647
# 2021深圳最低工资
SZ_MIN_SALARY = 2200

ListTaxPerMonth = []            # record each month tax, should be saved to file
ListIncomePerMonth = []         # record each month income (subtracted by tax), should be saved to file

# 下面两个年税率表和月税率表均针对应纳税额来查表
tax_ratio_dict_year = {'less_36000':[0.03,0],
                  'large_36000_less_144000':[0.1,2520],
                  'large_144000_less_300000':[0.2,16920],
                  'large_300000_less_420000':[0.25,31920],
                  'large_420000_less_660000':[0.3,52920],
                  'large_660000_less_960000':[0.35,85920],
                  'large_960000':[0.45,181920]}

tax_ratio_dict_month = {'less_3000':[0.03,0],
                  'large_3000_less_12000':[0.1,210],
                  'large_12000_less_25000':[0.2,1410],
                  'large_25000_less_35000':[0.25,2660],
                  'large_35000_less_55000':[0.3,4410],
                  'large_55000_less_80000':[0.35,7160],
                  'large_80000':[0.45,15160]}
'''
DictTaxDataPerMonth = {
    'month_index':0,
    'basic_salary':0,
    'transport_subsidy':0,
    'unemployment_insurance':0,
    'pension':0,
    'medical_insurance':0,
    'housing_fund':0,
    'year_total_elderly_exemption':0,
    'year_total_loan_exemption':0,
    'other_subsidy':0,
    'year_end_awards':
}
'''

DictTaxDataPerYear = {}

# 实际的数据和网络上查到数据有些差异,以实际数据为准
def FigureMonthTaxData(month_index, basic_salary, transport_subsidy, \
                       unemployment_insurance, pension, medical_insurance, housing_fund,\
                       other_subsidy = 0, year_end_awards = 0):
    DictTaxDataPerMonth = {}
    DictTaxDataPerMonth['month_index'] = int(month_index)
    DictTaxDataPerMonth['basic_salary'] = float(basic_salary)
    DictTaxDataPerMonth['transport_subsidy'] = float(transport_subsidy)
    DictTaxDataPerMonth['other_subsidy'] = float(other_subsidy)
    DictTaxDataPerMonth['year_end_awards'] = float(year_end_awards)
    DictTaxDataPerMonth['unemployment_insurance'] = float(unemployment_insurance)
    DictTaxDataPerMonth['pension'] = float(pension)
    DictTaxDataPerMonth['medical_insurance'] = float(medical_insurance)
    DictTaxDataPerMonth['housing_fund'] = float(housing_fund)
    DictTaxDataPerMonth['elderly_exemption'] = float(month_elderly_exemption)
    DictTaxDataPerMonth['loan_exemption'] = float(month_loan_exemption)
    DictTaxDataPerMonth['tax'] = 0

    # must use deepcopy, otherwise, the reference of DictTaxDataPerMonth is assigned, then all the item in
    # DictTaxDataPerYear will point to one DictTaxDataPerMonth
    DictTaxDataPerYear[month_index] = copy.deepcopy(DictTaxDataPerMonth)

    # 当月应缴税 = (到当月为止的总收入 - 当月为止的总免征额 - 当月为止三险一金总额 - 当月为止的专项附加扣除总额)*税率 - 速算扣除数
    year_total_income = 0
    for j in range(month_index):
        month_total_income = DictTaxDataPerYear[j+1]['basic_salary'] + DictTaxDataPerYear[j+1]['transport_subsidy'] + \
                            DictTaxDataPerYear[j+1]['other_subsidy'] + DictTaxDataPerYear[j+1]['year_end_awards']
        year_total_income += month_total_income

    '''
    year_total_income = DictTaxDataPerMonth['basic_salary'] + DictTaxDataPerMonth['transport_subsidy'] +\
                        DictTaxDataPerMonth['other_subsidy'] + DictTaxDataPerMonth['year_end_awards']
    '''

    year_total_exemption = month_index * exemption

    year_total_3_and_1 = 0
    for j in range(month_index):
        month_total_3_and_1 = DictTaxDataPerYear[j+1]['unemployment_insurance'] + DictTaxDataPerYear[j+1]['pension'] +\
                         DictTaxDataPerYear[j+1]['medical_insurance'] + DictTaxDataPerYear[j+1]['housing_fund']
        year_total_3_and_1 += month_total_3_and_1
    '''
    year_total_3_and_1 = DictTaxDataPerMonth['unemployment_insurance'] + DictTaxDataPerMonth['pension'] +\
                         DictTaxDataPerMonth['medical_insurance'] + DictTaxDataPerMonth['housing_fund']
    '''

    year_total_elderly_exemption = month_index * DictTaxDataPerMonth['elderly_exemption']

    year_total_loan_exemption = month_index * DictTaxDataPerMonth['loan_exemption']

    income_should_use = year_total_income - year_total_exemption - year_total_3_and_1 - year_total_elderly_exemption -\
                        year_total_loan_exemption

    print('The money should use is {}'.format(income_should_use))

    if income_should_use <= 36000:
        ratio_year_index = 'less_36000'
    elif income_should_use > 36000 and income_should_use <= 144000:
        ratio_year_index = 'large_36000_less_144000'
    elif income_should_use > 144000 and income_should_use <= 300000:
        ratio_year_index = 'large_144000_less_300000'
    elif income_should_use > 300000 and income_should_use <= 420000:
        ratio_year_index = 'large_300000_less_420000'
    elif income_should_use > 420000 and income_should_use <= 660000:
        ratio_year_index = 'large_420000_less_660000'
    elif income_should_use > 660000 and income_should_use <= 960000:
        ratio_year_index = 'large_660000_less_960000'
    else:
        ratio_year_index = 'large_960000'

    ls = tax_ratio_dict_year[ratio_year_index]

    tax_already_paid = 0
    if month_index == 1:
        DictTaxDataPerYear[1]['tax'] = income_should_use * ls[0] - ls[1]
    else:
        for j in range(month_index):
            tax_already_paid += DictTaxDataPerYear[j+1]['tax']
        tax_this_month = income_should_use * ls[0] - ls[1] - tax_already_paid
        DictTaxDataPerYear[month_index]['tax'] = tax_this_month


    print("The month {} tax should be paid is {}".format(month_index, DictTaxDataPerYear[month_index]['tax']))



'''
def FigureMonthTaxData(month_index, basic_salary, transport_subsidy, other_subsidy = 0, year_end_awards = 0):
    DictTaxDataPerMonth['month_index'] = month_index
    DictTaxDataPerMonth['basic_salary'] = basic_salary
    DictTaxDataPerMonth['transport_subsidy'] = transport_subsidy
    DictTaxDataPerMonth['other_subsidy'] = other_subsidy
    DictTaxDataPerMonth['year_end_awards'] = year_end_awards
    total_income = basic_salary + transport_subsidy + other_subsidy + year_end_awards
    if total_income >= GD_AVERAGE_SALARY:
        bench_income = GD_AVERAGE_SALARY * 3            # 三倍社平工资
    else:
        bench_income = total_income
    DictTaxDataPerMonth['unemployment_insurance'] = SZ_MIN_SALARY * 0.003
    DictTaxDataPerMonth['pension'] = bench_income * 0.08
    DictTaxDataPerMonth['medical_insurance'] = total_income * 0.02          #按收入总额算,没有按社平算
    DictTaxDataPerMonth['housing_fund'] = total_income * 0.12

    total_elderly_exemption = month_index * month_elderly_exemption
    total_loan_exemption = month_index * month_loan_exemption

    income_to_calc_tax = math.fsum(ListIncomePerMonth)

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

    tax_this_month =
'''





def main():
    # print(DictTaxDataPerMonth)
    FigureMonthTaxData(1, 30310.98, 200, 6.6, 1621.44, 577.36, 3832.56)
    FigureMonthTaxData(2, 30310.98, 200, 6.6, 1621.44, 610.22, 3832.56, 4108)
    FigureMonthTaxData(3, 30310.98, 200, 6.6, 1621.44, 610.22, 3832.56, 0)
    FigureMonthTaxData(4, 30310.98, 200, 6.6, 1621.44, 638.76, 3832.56, 0)
    print(DictTaxDataPerYear)

if __name__ == '__main__':
    '''
    '''
    main()