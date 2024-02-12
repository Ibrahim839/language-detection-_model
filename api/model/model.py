class Model:

    def __init__(self ,model_path):
        from joblib import load
        import re
        self.model = load(model_path)
        self.__version__ = re.findall(pattern=r'\d+.\d+.\d+', string = model_path)[0]
    @staticmethod
    def preprocess(X):
        from string import punctuation
        table = str.maketrans('' ,'' ,'0123456789' + punctuation)
        helper = lambda x: ' '.join(x.lower().translate(table).split())
        return [helper(x) for x in X]

    def predict(self ,x):
        X = Model.preprocess([x])
        return self.model.predict(X)[0]

import os
model = Model(f'{os.path.dirname(__file__)}/pipeline-0.1.0.pkl')


if __name__ == '__main__':
    print(model.predict('hallo'))
    print(model.__version__)