# Dados do amuleto
# Use o modo 'r+' para leitura e escrita, e garanta que o arquivo exista
try:
    f_mu = open('/home/tenfranciscoclaudio/Documentos/Python/Match_Ups.txt', 'r+')
    mu = f_mu.readlines()
except FileNotFoundError:
    print("O arquivo Match_Ups.txt não foi encontrado. Criando um novo.")
    with open('/home/tenfranciscoclaudio/Documentos/Python/Match_Ups.txt', 'w') as f:
        pass
    f_mu = open('/home/tenfranciscoclaudio/Documentos/Python/Match_Ups.txt', 'r+')
    mu = f_mu.readlines()

try:
    f_wr = open('/home/tenfranciscoclaudio/Documentos/Python/Win_Rates.txt', 'r+')
    wr = f_wr.readlines()
except FileNotFoundError:
    print("O arquivo Win_Rates.txt não foi encontrado. Criando um novo.")
    with open('/home/tenfranciscoclaudio/Documentos/Python/Win_Rates.txt', 'w') as f:
        pass
    f_wr = open('/home/tenfranciscoclaudio/Documentos/Python/Win_Rates.txt', 'r+')
    wr = f_wr.readlines()

# --- Funções do menu ---

def exibir_menu():
    """Exibe as opções do menu principal."""
    print("\n--- Menu Principal ---")
    print("1. Adicionar resultado")
    print("2. Consultar Win Rate")
    print("3. Consultar Matchup Específica")
    print("0. Sair do programa")

def adicionar_resultado():
    """Lógica para a opção 1: Adicionar resultado."""
    print("Você escolheu: Adicionar resultado\n")
    
    # Recarrega a lista de matchups para garantir que esteja atualizada
    f_mu.seek(0)
    mu = f_mu.readlines()
    
    i = 1
    vet_aux = []
    print("Matchups existentes:")
    for line in mu:
        line = line.strip()
        print(f"{i}. {line}")
        vet_aux.append(line)
        i += 1
    
    print("0. Adicionar nova Match Up")
    
    try:
        matchup_escolha = int(input("\nEscolha a Match Up: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return

    if matchup_escolha == 0:
        nova_matchup = input("Insira a nova Match Up: ").strip()
        if not nova_matchup:
            print("Nome da Match Up não pode ser vazio.")
            return
        
        # Adiciona a nova matchup ao arquivo de Match_Ups
        f_mu.write(f"{nova_matchup}\n")
        f_mu.flush() # Salva imediatamente as alterações
        nome_matchup = nova_matchup
    elif 1 <= matchup_escolha <= len(vet_aux):
        nome_matchup = vet_aux[matchup_escolha - 1]
    else:
        print("Opção de Match Up inválida.")
        return

    G1 = input("G1 (V para vitória, D para derrota, E para empate, 0 para não ocorreu): ").upper().strip()
    G2 = input("G2 (V para vitória, D para derrota, E para empate, 0 para não ocorreu): ").upper().strip()
    G3 = input("G3 (V para vitória, D para derrota, E para empate, 0 para não ocorreu): ").upper().strip()
    
    # Validação simples do resultado
    resultados = [G1, G2, G3]
    for r in resultados:
        if r not in ['V', 'D', 'E', '0']:
            print(f"Resultado inválido '{r}'. Por favor, use V, D, E ou 0.")
            return

    texto = f"{nome_matchup}: {G1} {G2} {G3}\n"
    f_wr.write(texto)
    f_wr.flush() # Salva imediatamente as alterações
    
    print("\nResultado adicionado com sucesso!")

def consultar_win_rate():
    """Lógica para a opção 2: Consultar Win Rate."""
    print("\nVocê escolheu: Consultar Win Rate")
    
    # Recarrega a lista de resultados para garantir que esteja atualizada
    f_wr.seek(0)
    wr = f_wr.readlines()
    
    if not wr:
        print("Sem dados para calcular as Win Rates.")
        return
    
    total_vitorias_por_jogo = {'G1': 0, 'G2': 0, 'G3': 0}
    total_jogos_jogados_por_jogo = {'G1': 0, 'G2': 0, 'G3': 0}
    total_partidas_vencidas = 0
    total_partidas_jogadas = 0

    for line in wr:
        try:
            _, resultado_str = line.split(': ')
            resultados_jogos = resultado_str.strip().split(' ')
            
            # Conta vitórias na partida para o cálculo da Win Rate de Partida
            vitorias_na_partida = resultados_jogos.count('V')
            if vitorias_na_partida >= 2:
                total_partidas_vencidas += 1
            total_partidas_jogadas += 1

            # Conta os resultados de cada jogo
            for i, r in enumerate(resultados_jogos):
                if r == 'V':
                    total_vitorias_por_jogo[f'G{i+1}'] += 1
                if r in ['V', 'D', 'E']:
                    total_jogos_jogados_por_jogo[f'G{i+1}'] += 1
        except (ValueError, IndexError):
            continue

    print("\n--- Win Rate por Jogo ---")
    for jogo, vitorias in total_vitorias_por_jogo.items():
        total = total_jogos_jogados_por_jogo[jogo]
        if total > 0:
            win_rate_jogo = (vitorias / total) * 100
            print(f"Win Rate {jogo}: {win_rate_jogo:.2f}% ({vitorias} Vitórias em {total} Jogos)")
        else:
            print(f"Win Rate {jogo}: Sem dados para calcular.")
    
    print("\n--- Win Rate de Partida (Match Win Rate) ---")
    if total_partidas_jogadas > 0:
        win_rate_partida = (total_partidas_vencidas / total_partidas_jogadas) * 100
        print(f"Win Rate de Partida: {win_rate_partida:.2f}% ({total_partidas_vencidas} Vitórias em {total_partidas_jogadas} Partidas)")
    else:
        print("Sem dados de partida para calcular a Win Rate.")

def consultar_matchup_especifica():
    """Lógica para a opção 3: Consultar Matchup Específica."""
    print("\nVocê escolheu: Consultar Matchup Específica")
    
    # Recarrega a lista de matchups para garantir que esteja atualizada
    f_mu.seek(0)
    mu = f_mu.readlines()
    
    # Recarrega a lista de resultados para garantir que esteja atualizada
    f_wr.seek(0)
    wr = f_wr.readlines()
    
    i = 1
    vet_aux = []
    print("Matchups existentes:")
    for line in mu:
        line = line.strip()
        print(f"{i}. {line}")
        vet_aux.append(line)
        i += 1
        
    try:
        matchup_escolha = int(input("\nEscolha a Match Up que deseja consultar: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return
    
    if 1 <= matchup_escolha <= len(vet_aux):
        matchup_escolhida = vet_aux[matchup_escolha - 1]
    else:
        print("Opção de Match Up inválida.")
        return

    # Adicionando o cálculo de Win Rate por matchup
    vitorias_matchup = 0
    derrotas_matchup = 0
    empates_matchup = 0
    total_jogos_matchup = 0

    print(f"\n--- Resultados para a Match Up: {matchup_escolhida} ---")
    
    encontrado = False
    for line in wr:
        if line.strip().startswith(matchup_escolhida + ':'):
            encontrado = True
            print(line.strip())
            
            try:
                _, resultado_str = line.split(': ')
                resultados_jogos = resultado_str.strip().split(' ')
                for r in resultados_jogos:
                    if r == 'V':
                        vitorias_matchup += 1
                    elif r == 'D':
                        derrotas_matchup += 1
                    elif r == 'E':
                        empates_matchup += 1
                    
                    if r != '0':
                        total_jogos_matchup += 1
            except (ValueError, IndexError):
                continue
            
    if encontrado:
        print("-" * 20)
        print("Estatísticas da Matchup:")
        print(f"  Vitórias: {vitorias_matchup}")
        print(f"  Derrotas: {derrotas_matchup}")
        print(f"  Empates: {empates_matchup}")
        print(f"  Total de Jogos: {total_jogos_matchup}")
        
        if total_jogos_matchup > 0:
            win_rate_matchup = (vitorias_matchup / total_jogos_matchup) * 100
            print(f"  Win Rate da Matchup: {win_rate_matchup:.2f}%")
        else:
            print("  Sem dados suficientes para calcular a Win Rate.")
    else:
        print(f"Nenhum resultado encontrado para a Match Up '{matchup_escolhida}'.")

# --- Loop principal do programa ---

def main():
    """Função principal que executa o menu interativo."""
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: \n")

        if opcao == '1':
            adicionar_resultado()
        elif opcao == '2':
            consultar_win_rate()
        elif opcao == '3':
            consultar_matchup_especifica()
        elif opcao == '0':
            print("Saindo do programa. Até mais!")
            f_mu.close()
            f_wr.close()
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Executa o programa
if __name__ == "__main__":
    main()

