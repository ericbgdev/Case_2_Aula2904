from db.database import get_connection
from model.usuario import Usuario


class UsuarioRepository:
    def salvar(self, usuario: Usuario) -> Usuario:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
            (usuario.nome, usuario.email)
        )
        conn.commit()
        usuario.id = cursor.lastrowid
        conn.close()
        return usuario

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios")
        rows = cursor.fetchall()
        conn.close()
        return [Usuario(r[1], r[2], r[0]) for r in rows]

    def buscar_por_id(self, usuario_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios WHERE id = ?", (usuario_id,))
        row = cursor.fetchone()
        conn.close()
        return Usuario(row[1], row[2], row[0]) if row else None

    def atualizar(self, usuario: Usuario) -> Usuario:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?",
            (usuario.nome, usuario.email, usuario.id)
        )
        conn.commit()
        conn.close()
        return usuario

    def deletar(self, usuario_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
        conn.commit()
        conn.close()
