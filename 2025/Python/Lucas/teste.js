// Bem-vindo ao JavaScript! Este é um comentário de linha única

/*
  Este é um comentário de múltiplas linhas
  JavaScript é uma linguagem de programação usada principalmente para web
*/

// 1. VARIÁVEIS - Três formas de declarar variáveis
let nome = "Lucas";           // Pode ser alterada
const idade = 25;            // Não pode ser alterada (constante)
var cidade = "São Paulo";    // Forma antiga (evite usar)

// 2. TIPOS DE DADOS
let texto = "Olá, mundo!";        // String (texto)
let numero = 42;                  // Number (número)
let decimal = 3.14;             // Number decimal
let booleano = true;            // Boolean (verdadeiro/falso)
let lista = [1, 2, 3, "quatro"]; // Array (lista)
let objeto = {                  // Object (objeto)
    chave: "valor",
    nome: "JavaScript",
    versao: 2023
};

// 3. FUNÇÕES - Blocos de código reutilizáveis
function saudacao(nome) {
    return "Olá, " + nome + "!";
}

// Arrow function (forma moderna)
const somar = (a, b) => {
    return a + b;
};

// Função simples de uma linha
const multiplicar = (a, b) => a * b;

// 4. CONDICIONAIS - Tomada de decisão
if (idade >= 18) {
    console.log("Você é maior de idade!");
} else {
    console.log("Você é menor de idade!");
}

// 5. LOOPS - Repetição
console.log("Contando de 1 a 5:");
for (let i = 1; i <= 5; i++) {
    console.log(i);
}

// 6. TRABALHANDO COM ARRAYS
let frutas = ["maçã", "banana", "laranja"];
frutas.push("uva"); // Adiciona no final
console.log("Frutas:", frutas);

// 7. TRABALHANDO COM OBJETOS
let pessoa = {
    nome: "Ana",
    idade: 30,
    profissao: "Desenvolvedora"
};
console.log(pessoa.nome + " tem " + pessoa.idade + " anos");

// 8. CHAMANDO FUNÇÕES
console.log(saudacao("Visitante"));
console.log("2 + 3 =", somar(2, 3));
console.log("4 × 5 =", multiplicar(4, 5));

// 9. TEMPLATE LITERALS (forma moderna de concatenar)
let mensagem = `Meu nome é ${nome}, tenho ${idade} anos e moro em ${cidade}`;
console.log(mensagem);

// 10. EXEMPLO PRÁTICO - Calculadora simples
function calculadora(num1, num2, operacao) {
    switch(operacao) {
        case '+':
            return num1 + num2;
        case '-':
            return num1 - num2;
        case '*':
            return num1 * num2;
        case '/':
            return num2 !== 0 ? num1 / num2 : "Erro: divisão por zero";
        default:
            return "Operação inválida";
    }
}

// Testando a calculadora
console.log("=== Calculadora ===");
console.log("10 + 5 =", calculadora(10, 5, '+'));
console.log("10 - 5 =", calculadora(10, 5, '-'));
console.log("10 × 5 =", calculadora(10, 5, '*'));
console.log("10 ÷ 5 =", calculadora(10, 5, '/'));

// DICA: Para executar este código:
// 1. Instale o Node.js em nodejs.org
// 2. Abra o terminal na pasta onde está este arquivo
// 3. Execute: node teste.js
