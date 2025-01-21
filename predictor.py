import chess
import chess.engine

def play_with_stockfish(is_white):
    board = chess.Board()
    print("La partie commence !")
    print(board)
    profondeur = 1

    stockfish_path = "stockfish"
    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        while not board.is_game_over():
            if is_white:
                result = engine.play(board, chess.engine.Limit(time=5.0))
                best_move = result.move
                print(f"Je vous conseille de jouer : {best_move}")
                board.push(best_move)
                print(board)
            else:
                if 1 != profondeur:
                    result = engine.play(board, chess.engine.Limit(time=1.0))
                    best_move = result.move
                    print(f"Je vous conseille de jouer : {best_move}")
                    board.push(best_move)
                    print(board)

            if board.is_game_over():
                break

            # Demander le coup de l'adversaire
            valid_move = False
            while not valid_move:
                user_input = input("Entrez le coup joué par votre adversaire (ex: Nf3 ou e5) : ")
                try:
                    move = board.parse_san(user_input)
                    if move in board.legal_moves:
                        board.push(move)
                        valid_move = True
                    else:
                        print("Coup illégal, essayez à nouveau.")
                except ValueError as e:
                    print(f'Erreur : {e}')

            if board.is_game_over():
                break

            print(board)
            profondeur += 1

        if board.is_checkmate():
            print("Échec et mat !")
        elif board.is_stalemate():
            print("Pat !")
        else:
            print("Partie terminée.")

if __name__ == '__main__':
    color = input("Êtes-vous les Blancs ou les Noirs ? (b/n) : ").strip().lower()
    is_white = color == 'b'
    play_with_stockfish(is_white)
