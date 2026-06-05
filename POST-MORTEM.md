# Post-Mortem — Missão de Release

## Time

* Tech Lead: Guilherme Ryan
* Dev A: Guilherme Pinheiro
* Dev B: Felipe Eduardo
* QA/Release: William Gomes

---

## O que funcionou bem

A divisão das tarefas permitiu que nossa equipe pudesse colaborar de forma mais organizada e eficiente no codigo. O uso das branches separadas para cada funcionalidade também ajudou muito a manter o código organizado e facilitou a revisão das alterações por meio dos Pull Requests. Era muito simples de identificar onde estava cada erro e diferença entre os códigos. Também conseguimos entender e aplicar corretamente o fluxo de desenvolvimento utilizando as branches `feature/dev-a`, `feature/dev-b`, `develop`, `release/1.0` e `main`.

---

## O que deu errado ou foi difícil

A principal dificuldade foi a resolução do conflito durante o rebase, porque os dois desenvolvedores modificaram as funções ao mesmo tempo. Foi necessário analisar as alterações dos dois para combinar as funcionalidades sem perder código e nem documentação. Além disso, foi um pouco complexo entender onde colocar o bug e se seria necessário criar uma branch adicional para tal. Outra dificuldade foi entender o fluxo correto do hotfix e garantir que a correção fosse aplicada tanto na `main` quanto na `develop`. 

---

## Onde usamos rebase (e por quê)

Utilizamos `git rebase develop` nas branches de feature antes da abertura dos Pull Requests. Ele foi utilizado para atualizar as branches dos desenvolvedores com as alterações mais recentes da `develop`, mantendo um histórico mais linear e permitindo identificar e resolver conflitos antes da integração final.O conflito ocorreu principalmente na branch do Dev B, pois as alterações do Dev A já haviam sido incorporadas à `develop` por meio do Pull Request.

---

## Onde usamos merge (e por quê)

Utilizamos merge durante a integração dos Pull Requests das branches `feature/dev-a` e `feature/dev-b` para a branch `develop`. Utilizamos merge para integrar o `release/1.0` na `main`. Também utilizamos merge durante o processo de hotfix, integrando a correção da branch `hotfix/fix-filter` na `main` e depois na `develop`. Além disso, no final, para documentar o changelog e post-mortem foi usado o merge novamente para integrar a documentação do `develop` a `main`. O merge foi utilizado para preservar o histórico das integrações e registrar claramente quando cada funcionalidade foi incorporada ao projeto. 

---

## O que faríamos diferente

Planejaríamos melhor as alterações realizadas em arquivos compartilhados para reduzir a quantidade de conflitos durante a integração. Também documentaríamos o fluxo de branches desde o início do projeto para facilitar a compreensão das responsabilidades de cada integrante e reduzir dúvidas durante o processo de release e hotfix que tivemos mais dificuldade.
