# data_anonymization.py

import pandas as pd
import numpy as np

class DataAnonymization:
    def __init__(self, data):
        """
        Initialize the DataAnonymization class with a DataFrame.
        
        :param data: A pandas DataFrame containing the data to be anonymized.
        """
        self.data = data

    def k_anonymity(self, k):
        """
        Apply k-anonymity to the dataset.
        
        :param k: The minimum group size for k-anonymity.
        :return: A DataFrame that satisfies k-anonymity.
        """
        # Generalize the data to ensure k-anonymity
        generalized_data = self.data.copy()
        
        # Generalization example: replace specific values with ranges or categories
        for column in generalized_data.columns:
            if generalized_data[column].dtype in [np.int64, np.float64]:
                # Example: generalize numerical data to ranges
                generalized_data[column] = pd.cut(generalized_data[column], bins=5, labels=False)
            else:
                # Example: generalize categorical data by taking the first letter
                generalized_data[column] = generalized_data[column].apply(lambda x: str(x)[0] + '*')

        # Filter groups that have at least k entries
        k_anonymous_data = generalized_data.groupby(list(generalized_data.columns)).filter(lambda x: len(x) >= k)
        return k_anonymous_data

    def differential_privacy(self, epsilon):
        """
        Apply differential privacy to the dataset by adding noise.
        
        :param epsilon: The privacy budget parameter.
        :return: A DataFrame with added noise for differential privacy.
        """
        noisy_data = self.data.copy()
        
        # Adding Laplace noise to numerical columns
        for column in noisy_data.select_dtypes(include=[np.int64, np.float64]).columns:
            scale = 1 / epsilon  # Scale for Laplace noise
            noise = np.random.laplace(0, scale, size=noisy_data[column].shape)
            noisy_data[column] += noise
        
        return noisy_data

# Example usage
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        'age': [25, 30, 35, 40, 25, 30, 35, 40],
        'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
        'income': [50000, 60000, 70000, 80000, 50000, 60000, 70000, 80000]
    })

    anonymizer = DataAnonymization(data)

    # Apply k-anonymity
    k_anonymous_data = anonymizer.k_anonymity(k=2)
    print("K-Anonymized Data:")
    print(k_anonymous_data)

    # Apply differential privacy
    private_data = anonymizer.differential_privacy(epsilon=0.5)
    print("\nData with Differential Privacy:")
    print(private_data)
