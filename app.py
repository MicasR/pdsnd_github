from data_analysis import formater, data, analysis
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Render Query page."""
    return render_template("index.html")


@app.route("/Dashboard")
def dashboard():
    "Gether analysis and render on dashboard."
    formated_filters = formater.format_filters(request.args.to_dict())
    df = data.filter_data(formated_filters)
    stats = analysis.analyze(df)

    if df.empty:
        data_stream = {}
    else:
        data_stream = df.iloc[:15, :].to_dict()

    return render_template(
        "dashboard.html",
        formated_filters=formated_filters,
        stats=stats,
        data_stream=data_stream
    )


@app.route("/Stream Data", methods=['POST'])
def stream_data()  -> dict:
    """From a filters dict and a page number return a dict with a stream of data."""
    req_params = request.get_json()
    df = data.filter_data(req_params["filters"])
    data_stream = {}
    start_at = 0
    end_at = 0

    if not df.empty and req_params["page"] >=1:
        end_at = req_params["page"] * req_params["rowsPerPage"]
        start_at = ((req_params["page"] -1) * req_params["rowsPerPage"])

    data_stream = df.iloc[start_at:end_at, :].to_dict()

    return {
        "data_stream": data_stream,
        "rowsPerPage": req_params["rowsPerPage"],
        "page": req_params["page"]
    }
