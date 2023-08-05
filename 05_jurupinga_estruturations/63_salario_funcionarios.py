cargos = []
def addCargo(cargo,salario,inss,convenio):
    cargos.append({
        "cargo":cargo,
        "salario":salario,
        "inss_percent":inss,
        "convenio":convenio
    })
addCargo("Gerente",5590,8,289)
addCargo("Supervisor",4128,7,239)
addCargo("Técnico",3789,4,189)
addCargo("Auxiliar",2345,2,156)

for cargo in cargos:
    valor_inss = cargo.get("salario") / 100 * cargo.get("inss_percent")
    desconto_total = cargo.get("convenio") + valor_inss
    salario_liq = cargo.get("salario") - desconto_total
    print(f'Cargo: {cargo.get("cargo")} \nSalario Liquido: R${salario_liq:.2f}\n')