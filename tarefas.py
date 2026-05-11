tarefas = []
 
def cadastrar_tarefa():
    print("\n=== CADASTRAR NOVA TAREFA ===")
    descricao = input("Descrição da tarefa: ")
    vencimento = input("Data de vencimento (dd/mm/aaaa): ")

#status inicial sempre "pendente"
    tarefa = {
        'id': len(tarefas) + 1,
        'descricao': descricao,
        'vencimento': vencimento,
        'status': 'pendente'
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")
 
def listar_tarefas():
    print("\n=== LISTAGEM DE TAREFAS ===")
    
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("1 - Listar todas")
    print("2 - Filtrar por status")
    print("3 - Filtrar por data de vencimento")
    opcao = input("Escolha uma opção: ")