egyik = input('adj meg egy szót!!')
egyik_hossz = len(egyik)
masik = input('adj meg egy szót!!')
masik_hossz = len(masik)

if egyik_hossz > masik_hossz:
    print(f'az első szó hosszabb, mert {egyik_hossz} karakterből áll')
if egyik_hossz < masik_hossz:
    print(f'a második szó hosszabb, mert {masik_hossz} karakterből áll')