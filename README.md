<!DOCTYPE html>
<html>
<head>
    <title>Título Digitado Estilizado</title>
    <style>
        /* Estilo para o texto digitado */
        .typed-text {
            color: purple;
            overflow: hidden;
            white-space: nowrap;
            border-right: 0.15em solid purple;
            animation: typing 3s steps(40) infinite;
        }

        /* Animação de digitação */
        @keyframes typing {
            from {
                width: 0;
            }
            to {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <h1 class="typed-text">Título Estilizado em Roxo</h1>
    <script>
        // Função para exibir o texto com animação de digitação
        function typeEffect() {
            const text = document.querySelector('.typed-text');
            const words = ['Título Estilizado em Roxo'];

            let i = 0;
            let j = 0;
            let currentWord = '';
            let isDeleting = false;

            function type() {
                if (i === words.length) {
                    i = 0;
                }

                currentWord = words[i];

                if (isDeleting) {
                    text.textContent = currentWord.substring(0, j - 1);
                    j--;
                } else {
                    text.textContent = currentWord.substring(0, j + 1);
                    j++;
                }

                if (!isDeleting && j === currentWord.length) {
                    isDeleting = true;
                    setTimeout(type, 1000);
                } else if (isDeleting && j === 0) {
                    isDeleting = false;
                    i++;
                    setTimeout(type, 500);
                } else {
                    setTimeout(type, 80);
                }
            }

            type();
        }

        typeEffect();
    </script>
</body>
</html>

</br>
</br>
</br>
</br>
</br>
## Imagem do modelo relacional e da explicação lógica do funcionamento.
[![52140d88-e193-432c-a911-bc554ff52c4b.jpg](https://i.postimg.cc/0QyN0xng/52140d88-e193-432c-a911-bc554ff52c4b.jpg)](https://postimg.cc/VS21zx24)
