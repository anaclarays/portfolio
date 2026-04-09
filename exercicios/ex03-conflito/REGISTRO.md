## Resolução de Conflito

### O que causou o conflito

O conflito ocorreu no arquivo `conflito.txt`, dentro da pasta `ex03-conflito`. Ele foi gerado porque duas *branches* diferentes realizaram alterações no mesmo trecho do arquivo.

Enquanto uma *branch* modificou o conteúdo para uma versão específica, a outra *branch* alterou exatamente a mesma linha para um conteúdo diferente. Como o Git não consegue decidir automaticamente qual versão deve prevalecer, ele sinaliza esse conflito durante o *merge*.

O arquivo ficou marcado da seguinte forma:

```text
<<<<<<< HEAD
alteração da branch atual
=======
alteração da outra branch
>>>>>>> nome-da-branch
```

---

### Como decidi qual versão manter

A decisão foi baseada no objetivo final do arquivo dentro do contexto do exercício, então optei por manter a que fazia mais sentido para o resultado esperado.

---

### Como o conflito foi resolvido

Após editar o arquivo e definir a versão final, utilizei os seguintes comandos no terminal para marcar o conflito como resolvido:

```bash id="r6d74j"
git add exercicios/ex03-conflito/conflito.txt
git commit -m "resolvendo conflito no arquivo conflito.txt"
```

O comando `git add` indica ao Git que o conflito foi resolvido, e o `git commit` finaliza o processo, registrando a versão corrigida no histórico do repositório.

---
