import flask_xstatic_files as fx


def test_url_for(app):
    xsf = fx.XStaticFiles(app)
    with app.test_request_context():
        assert xsf.url_for('jquery', 'jquery.min.js') == '/xstatic/jquery/jquery.min.js'


def test_serve(app):
    xsf = fx.XStaticFiles(app)

    @app.route('/xstatic/<module>/<path:filename>')
    def xstatic(module, filename):
        return xsf.serve_or_404(module, filename)

    c = app.test_client()
    resp = c.get('/xstatic/jquery/exist')
    assert resp.status_code == 404

    resp = c.get('/xstatic/jquery/jquery.min.js')
    assert resp.status_code == 200
