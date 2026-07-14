class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo.lower()  # Normaliza para facilitar comparação
    
    def atacar(self):
        # Mapeamento dos ataques (apenas o que vem depois de "usando")
        ataques = {
            "mago": "magia",
            "guerreiro": "espada",
            "monge": "artes marciais",
            "ninja": "shuriken"
        }
        
        # Obtém o ataque ou mensagem padrão
        ataque = ataques.get(self.tipo, "um ataque genérico")
        
        # Mensagem corrigida (sem redundância)
        print(f"o {self.tipo} atacou usando {ataque}")


# ==================== TESTE ====================
if __name__ == "__main__":
    print("=== Ataques dos Heróis ===\n")
    
    mago = Heroi("Gandalf", 150, "Mago")
    guerreiro = Heroi("Arthur", 35, "Guerreiro")
    monge = Heroi("Bruce", 40, "Monge")
    ninja = Heroi("Hayato", 28, "Ninja")
    
    mago.atacar()
    guerreiro.atacar()
    monge.atacar()
    ninja.atacar()