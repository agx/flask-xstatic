import flask_xstatic as fx


def test_url_for(app):
    xs = fx.XStaticFiles(app)
    with app.test_request_context():
        assert xs.url_for('jquery', 'jquery.min.js') == '/xstatic/jquery/jquery.min.js'


def test_serve(app):
    xs = fx.XStaticFiles(app)

    @app.route('/xstatic/<module>/<path:filename>')
    def xstatic(module, filename):
        return xs.serve_or_404(module, filename)

    c = app.test_client()
    resp = c.get('/xstatic/jquery/exist')
    assert resp.status_code == 404

    resp = c.get('/xstatic/jquery/jquery.min.js')
    assert resp.status_code == 200
