from flask import Flask, render_template, request, json, jsonify
from fifteen import FifteenSolver

app = Flask(__name__)


@app.route('/')
def fifteen():
    """Render Fifteen Puzzle view."""
    return render_template("fifteen.html")

@app.route('/solve')
def solve():
    response_data = {'result': []}
    board_msg = request.args.get('board', None)

    if board_msg:
        board_arr = json.loads(board_msg)
        solver = FifteenSolver(4, 4, board_arr)
        move_str = solver.solve_puzzle();
        response_data['result'] = list(move_str)

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
