Feature: Teste de Automação do Formulário de Inscrição

  Scenario: Inscrição de estudante, curso e disciplinas no site
    Given Eu estou na página inicial "https://tdd-detroid.onrender.com/"
    When Eu espero que o overlay de carregamento desapareça
    And Eu clico no campo "Nome do Estudante"
    And Eu insiro "douglas" no campo "Nome do Estudante"
    And Eu clico no botão "Adicionar Estudante"
    Then Eu vejo a mensagem "INFO Added student id: 1, Name: douglas"

    When Eu clico no campo "Nome do Curso"
    And Eu insiro "mat" no campo "Nome do Curso"
    And Eu clico no botão "Adicionar Curso"
    Then Eu vejo a mensagem "INFO Added student id: 1, Name: douglas"

    When Eu clico no campo "ID do Estudante"
    And Eu insiro "1" no campo "ID do Estudante"
    And Eu clico no campo "ID do Curso"
    And Eu insiro "1" no campo "ID do Curso"
    And Eu clico no botão "Adicionar Curso"
    Then Eu vejo a mensagem "INFO Added student id: 1, Name: douglas"

    When Eu clico no campo "Nome da Disciplina"
    And Eu insiro "mat" no campo "Nome da Disciplina"
    And Eu clico no campo "ID do Curso da Disciplina"
    And Eu insiro "1" no campo "ID do Curso da Disciplina"
    And Eu clico no botão "Adicionar Disciplina"
    Then Eu vejo a mensagem "FAIL Necessários 3 cursos para se criar a primeira matéria"

    When Eu clico no campo "Nome do Curso"
    And Eu insiro "port" no campo "Nome do Curso"
    And Eu clico no botão "Adicionar Curso"
    And Eu clico no campo "Nome do Curso" novamente
    And Eu insiro "geo" no campo "Nome do Curso"
    And Eu clico no botão "Adicionar Curso"
    And Eu clico no botão "Adicionar Disciplina" novamente
    Then Eu vejo a mensagem "INFO Added discipline id: 1, Name: mat, Course: 1"

    When Eu clico no campo "Nome da Disciplina"
    And Eu insiro "mat2" no campo "Nome da Disciplina"
    And Eu clico no botão "Adicionar Disciplina"
    And Eu clico no campo "Nome da Disciplina" novamente
    And Eu insiro "mat3" no campo "Nome da Disciplina"
    And Eu clico no botão "Adicionar Disciplina"
    And Eu clico no campo "ID do Estudante para Inscrição"
    And Eu insiro "1" no campo "ID do Estudante para Inscrição"
    And Eu clico no campo "ID da Disciplina para Inscrição"
    And Eu insiro "1" no campo "ID da Disciplina para Inscrição"
    And Eu clico no botão "Inscrever Estudante na Disciplina"
    Then Eu vejo a mensagem "WARN Aluno deve se inscrever em 3 materias no minimo"