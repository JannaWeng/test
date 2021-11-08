import flask
from google.cloud import bigquery

bigquery_client = bigquery.Client()

app = flask.Flask(__name__)


@app.route('/')
def main():

    query_job = bigquery_client.query(
        """
        SELECT CAST(Month AS DATE) AS Month, ROUND(Predicted_value, 3) AS Predicted_value 
        FROM `test123-331503.HDPE.HDPE_PREDICTION` 
        """
    )
    res = query_job.result()

    output = {}

    for row in res:
        output[str(row["Month"])] = row["Predicted_value"]

    return output

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)