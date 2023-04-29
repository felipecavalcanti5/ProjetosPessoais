# Com o presente programa, é possível saber exatamente os intervalos de páginas de um PDF qualquer para imprimir 
# duas páginas por folha. É necessário de antemão configurar a sessão "Dimensionamento de páginas e manuseio do 
# leitor de PDF para a opção "Múltiplo". 



inicio = int(input("Digite a página inicial: "))
final = int(input("Digite a página final: "))


if (final - inicio) % 2 != 0:
    for n in range(inicio, final + 1, +4):
        print("{}-{}; ".format(n, (n + 1)),end=' ')

if (final - inicio) % 2 == 0:
    for n in range(inicio, final - 1, +4):
        print("{}-{}; ".format(n, (n + 1)),end=' ')
    if final != (n+2):
        print(f"{final}", end=' ')

print('')

if (final - inicio) % 2 != 0:
    for n in range(inicio + 2, final + 1, +4):
        print("{}-{}; ".format(n, (n + 1)),end=' ')    

if (final - inicio) % 2 == 0:
    for n in range(inicio + 2, final - 1, +4):
        print("{}-{}; ".format(n, (n + 1)),end=' ')
    if final != (n+2):
        print(f"{final}", end=' ')

    
    
