#João Pedro Mendes Nowicki - Matricula: 202308232746.
#Rafael Kahl Konorath - Matricula: 202308232711.

class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print("Contato já existe!")
        else:
            self.contatos[nome] = telefone
            print("Contato adicionado com sucesso!")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado!")

    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"Nome: {nome}, Telefone: {self.contatos[nome]}")
        else:
            print("Contato não encontrado!")

    def listar_contatos(self):
        if not self.contatos:
            print("Agenda está vazia!")
        else:
            for nome, telefone in self.contatos.items():
                print(f"Nome: {nome}, Telefone: {telefone}")

def menu():
    agenda = AgendaTelefonica()
    while True:
        print("Bem Vindo a sua agenda pessoal com Alzheimer!! Depois de finalizado o programa esquecera tudo!!")
        print("Menu:")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Pesquisar contato")
        print("4. Listar contatos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif opcao == "2":
            nome = input("Digite o nome do contato: ")
            agenda.remover_contato(nome)
        elif opcao == "3":
            nome = input("Digite o nome do contato: ")
            agenda.pesquisar_contato(nome)
        elif opcao == "4":
            agenda.listar_contatos()
        elif opcao == "5":
            print("Obrigado por usar a agenda telefônica!")
            break
        else:
            print("Opção inválida. Tente novamente!")
menu()