def calc_sal(**kwargs):
    sal = kwargs.get("salario")
    desc_inss = kwargs.get("inss") / 100
    desc_plan_sau = kwargs.get("plano")
    desc_total = desc_inss + desc_plan_sau
    sal_liq = sal - desc_total
    print(f"Salario Liquido: {sal_liq}")
    print(f"Salario Bruto: {sal}")
calc_sal(salario=8000,inss=8,plano=130)
