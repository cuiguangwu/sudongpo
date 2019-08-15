class Model:
    def __init__(self,layers,type,inputsize,outputsize):
        self.layers = layers
        self.type = type
        self.inputsize = inputsize
        self.outputsize = outputsize

    def create_model(self,model):
        class Model(object):
            def __init__(self):
                pass
            def __call__(self):
                pass
        return Model

    def train(self,lr,batch_size,epoches):
        pass

    def test(self,lr,batch_size,epoches):
        pass
