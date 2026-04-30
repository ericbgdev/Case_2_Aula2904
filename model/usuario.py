class Usuario:
    def __init__(self, nome: str, email: str, id: int = None):
        self.id = id
        self.nome = nome
        self.email = email

    def to_dict(self) -> dict:
        return {"id": self.id, "nome": self.nome, "email": self.email}
