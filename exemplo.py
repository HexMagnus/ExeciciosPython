#vamos criar uma classe para clientes da Netflix
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in lista_planos:
            self.plano = plano
        else:
            print("Plano Inválido")
            raise Exception("Plano inválido")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano Inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver Filme {filme}")
        elif self.plano== "premium":
            print(f"Ver Filme {filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print ("Faça upgrade para premium para ver esse filme")
        else:
            print("Plano Inválido")

cliente = Cliente("Lucas", "exemplog@gmail.com", "basic")
print(cliente.plano)
cliente.ver_filme("Harry Potter", "premium")

#no botao de upgrade
cliente.mudar.plano("premium")
print(cliente.plano)


