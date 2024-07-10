from pipelines.training_pipeline import train_pipeline

if __name__ == "__main__":
    # run the pipeline
    train_pipeline(data_path="Customer_Satisfaction/archive_data/olist_order_reviews_dataset.csv")