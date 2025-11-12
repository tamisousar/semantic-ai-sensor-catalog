## ✨ COLINHA - Enviar tudo para o GitHub

### 1. Verificar o que mudou

```bash
git status
```

Mostra os arquivos modificados, novos ou prontos para enviar.

---

### 2. Adicionar todos os arquivos modificados

```bash
git add .
```

(O ponto significa "adiciona tudo nesta pasta").

---

### 3. Criar o commit

```bash
git commit -m "mensagem explicando o que foi feito"
```

Exemplo:

```bash
git commit -m "Update AI enrichment logic and add API folder"
```

---

### 4. Enviar para o GitHub

```bash
git push origin main
```

Tudo será salvo no repositório remoto.

---

### 5. Confirmar no GitHub

Acesse o repositório e atualize a página (⌘ + R).
Você verá seu commit e data **"just now"**.

---

### 🔁 Resumo rápido (modo turbo)

```bash
git add .
git commit -m "atualização"
git push origin main
```

---

### 💡 Extras úteis

| Comando             | O que faz                                   |
| ------------------- | ------------------------------------------- |
| `git pull`          | Baixa mudanças do GitHub pro seu computador |
| `git log --oneline` | Mostra histórico de commits resumido        |
| `git diff`          | Mostra o que foi alterado antes do commit   |

---

### 🚫 Ignorar arquivos do macOS

Crie um arquivo `.gitignore` e adicione:

```
# macOS system files
.DS_Store
```
