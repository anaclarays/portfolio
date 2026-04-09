# 🧠 Reflexão sobre o exercício

## O que foi difícil

Um dos principais pontos de dificuldade foi organizar os commits seguindo o padrão de *Conventional Commits*. No dia a dia, escrever uma mensagem mais direta no próprio commit acaba sendo mais rápido e prático do que elaborar descrições mais detalhadas em um *pull request*, por exemplo. Durante as tentativas, também houve certa confusão sobre onde exatamente aplicar esse padrão: se deveria estar no nome da *branch* ou na mensagem do commit em si. Apesar disso, percebo que é uma dificuldade superável com a prática contínua, já que se trata mais de criar o hábito do que de entender um conceito complexo.

Outro ponto que se destacou como mais desafiador foi a geração de conflitos entre *branches*. No início, não ficou muito claro como criar duas *branches* “ao mesmo tempo”, realizar alterações nelas e, em seguida, provocar um conflito durante o *merge*. Embora eu tenha conseguido gerar o conflito ao final, o processo até chegar lá não foi totalmente compreendido. Além disso, a resolução do conflito também não foi simples, exigindo mais atenção e entendimento do que exatamente estava acontecendo no código e nas versões envolvidas.

---

## O que ficou claro

A organização dos arquivos foi um aspecto que se mostrou mais intuitivo. A estruturação do projeto como um todo também ficou bem compreensível, o que contribui para uma melhor visualização e manutenção do repositório.

A criação de *branches* foi um conceito novo, mas relativamente simples de entender. Ficou evidente como essa prática beneficia o trabalho em equipe, tanto em termos de organização quanto na redução de erros, já que permite o desenvolvimento isolado antes da integração com a *branch* principal (`main`).

A realização de *pull requests* também se tornou mais clara ao longo do processo. Foi possível perceber sua importância antes de realizar o *merge*, principalmente como uma etapa de revisão que ajuda a evitar problemas maiores, incluindo conflitos quando há alterações nos mesmos arquivos em diferentes *branches*.

Por fim, a documentação foi uma parte mais tranquila, pois envolve sintetizar as informações do projeto em arquivos como o `README.md`, o que, apesar de exigir organização, não apresentou grandes dificuldades.

---

## O que ainda é confuso

A geração e, principalmente, a resolução de conflitos durante o *merge* ainda não estão totalmente claras. Alguns comandos, como:

```bash
git merge <nome-da-branch>
```

utilizados no terminal do VS Code, ainda geram dúvidas quanto ao seu funcionamento interno. Também permanece a incerteza sobre como trabalhar com duas *branches* em paralelo, realizando alterações sem enviá-las imediatamente ao repositório remoto e, posteriormente, integrá-las de forma segura. Além disso, decidir qual versão final deve prevalecer em um conflito ainda é um ponto que exige mais prática.

Outro aspecto que ainda causa dificuldade é o uso de caminhos no terminal. Em alguns momentos, houve problemas para localizar e acessar arquivos corretamente, o que impactou diretamente na execução das tarefas, como a própria criação de conflitos.

Por fim, o fluxo entre o ambiente local e o remoto ainda não está totalmente consolidado. Em algumas situações, as atualizações não apareceram corretamente no VS Code, o que acabou gerando confusão, retrabalho e a sensação de perda de progresso.
