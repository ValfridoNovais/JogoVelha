let currentPlayer; // Variável para armazenar o jogador atual
let gameState; // Variável para armazenar o estado do jogo (tabuleiro)
let player1; // Variável para armazenar o nome do Jogador 1
let player2; // Variável para armazenar o nome do Jogador 2

// Evento para iniciar o jogo quando o botão é clicado
document.getElementById('start').onclick = function() {
    player1 = document.getElementById('player1').value || 'Jogador 1'; // Obtém o nome do Jogador 1 ou usa padrão
    player2 = document.getElementById('player2').value || 'Jogador 2'; // Obtém o nome do Jogador 2 ou usa padrão
    startGame(); // Chama a função para iniciar o jogo
};

// Função para iniciar o jogo
function startGame() {
    gameState = ['', '', '', '', '', '', '', '', '', '']; // Inicializa o tabuleiro vazio
    currentPlayer = 'X'; // Define o jogador inicial como 'X'
    document.getElementById('board').style.display = 'grid'; // Exibe o tabuleiro
    document.getElementById('restart').style.display = 'inline-block'; // Exibe o botão de reiniciar
    document.querySelector('.form-group').style.display = 'none'; // Esconde o formulário de entrada

    const board = document.getElementById('board'); // Obtém o elemento do tabuleiro
    board.innerHTML = ''; // Limpa o conteúdo do tabuleiro
    for (let i = 0; i < 9; i++) { // Loop para criar 9 botões
        createButton(i); // Chama a função para criar um botão
    }
}

// Função para criar um botão no tabuleiro
function createButton(index) {
    const button = document.createElement('button'); // Cria um novo botão
    button.className = 'btn btn-custom'; // Adiciona classes de estilo ao botão
    button.onclick = () => handleClick(index); // Define a função a ser chamada ao clicar
    button.innerHTML = `<div class="shadow"></div>`; // Adiciona a sombra ao botão
    document.getElementById('board').appendChild(button); // Adiciona o botão ao tabuleiro
}

// Função para lidar com o clique em um botão do tabuleiro
function handleClick(index) {
    if (gameState[index] === '') { // Verifica se a posição está vazia
        gameState[index] = currentPlayer; // Marca a posição com o jogador atual
        updateBoard(); // Atualiza a visualização do tabuleiro
        checkWinner(); // Verifica se há um vencedor
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X'; // Alterna o jogador
    }
}

// Função para atualizar o tabuleiro visualmente
function updateBoard() {
    const buttons = document.getElementsByClassName('btn-custom'); // Obtém todos os botões do tabuleiro
    for (let i = 0; i < gameState.length; i++) { // Loop pelo estado do jogo
        buttons[i].innerHTML = gameState[i] || `<div class="shadow"></div>`; // Atualiza o botão com o símbolo do jogador ou sombra
    }
}

// Função para verificar se há um vencedor
function checkWinner() {
    // Conjuntos de posições que representam uma vitória
    const winningCombinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Colunas
        [0, 4, 8], [2, 4, 6] // Diagonais
    ];

    for (let combination of winningCombinations) { // Loop pelas combinações de vitória
        const [a, b, c] = combination; // Desestrutura as posições
        if (gameState[a] && gameState[a] === gameState[b] && gameState[a] === gameState[c]) { // Verifica se todas têm o mesmo valor
            alert(`${currentPlayer === 'X' ? player1 : player2} ganhou!`); // Exibe mensagem de vitória
            resetGame(); // Reinicia o jogo
            return; // Sai da função
        }
    }

    // Verifica se o tabuleiro está cheio e não há vencedor
    if (!gameState.includes('')) { // Se não há posições vazias
        alert("Empate!"); // Exibe mensagem de empate
        resetGame(); // Reinicia o jogo
    }
}

// Função para reiniciar o jogo
function resetGame() {
    gameState = ['', '', '', '', '', '', '', '', '', '']; // Reinicializa o estado do jogo
    updateBoard(); // Atualiza a visualização do tabuleiro
    currentPlayer = 'X'; // Reseta o jogador atual para 'X'
}

// Evento para reiniciar o jogo ao clicar no botão
document.getElementById('restart').onclick = resetGame;

// Função para mostrar e esconder a sidebar
document.getElementById('toggle-sidebar').onclick = function() {
    const sidebar = document.getElementById('sidebar'); // Obtém a sidebar
    sidebar.classList.toggle('hidden'); // Alterna a classe 'hidden' para mostrar/esconder
    if (sidebar.classList.contains('hidden')) { // Se a sidebar está escondida
        this.innerHTML = '≡'; // Define ícone de menu
    } else {
        this.innerHTML = '×'; // Define ícone de fechar
    }
};
