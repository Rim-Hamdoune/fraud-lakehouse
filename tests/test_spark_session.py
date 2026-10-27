"""Test de fumée : vérifie que PySpark démarre et calcule en local."""

from pyspark.sql import SparkSession


def test_spark_compte_les_lignes() -> None:
    spark = (
        SparkSession.builder.master("local[2]")
        .appName("test-fumee")
        .config("spark.driver.memory", "1g")
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )
    try:
        df = spark.createDataFrame(
            [(1, "TRANSFER"), (2, "CASH_OUT"), (3, "PAYMENT")],
            ["id", "type"],
        )
        assert df.count() == 3
    finally:
        spark.stop()
