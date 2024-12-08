import pandas as pd

class Analytics:
    @staticmethod
    def generate_summary_statistics(data):
        df = pd.DataFrame(data)
        return {
            'mean': df.mean().to_dict(),
            'median': df.median().to_dict(),
            'std_dev': df.std().to_dict(),
            'count': df.count().to_dict()
        }

    @staticmethod
    def correlation_matrix(data):
        df = pd.DataFrame(data)
        return df.corr().to_dict()

    @staticmethod
    def generate_report(data):
        summary = Analytics.generate_summary_statistics(data)
        correlation = Analytics.correlation_matrix(data)
        return {
            'summary': summary,
            'correlation': correlation
        }

# Usage
# report = Analytics.generate_report([[1, 2], [3, 4], [5, 6]])
