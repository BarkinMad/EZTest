class EZTest:
    def __init__(self):
        self.total = 0
        self.failed = 0
        
    def test(self, msg, expected, computed):
        '''
        Tests a computed value against the expected one
        Failure rate is stored
        '''
        
        if expected != computed:
            print ('Test Failure: ' + msg)
            self.failed += 1
        self.total += 1
    
    def __str__(self):
        if self.total - self.failed == 0:
            return 'No tests preformed.'
        return 'Preformed {} test{}, with {} failures. {}% Succsessful'.format(self.total, ('s' if self.total != 1 else ''), self.failed, round((float(self.total - self.failed) / float(self.total)) * 100))
            
    def reset(self):
        '''
        Resets logged failures to 0
        '''
        
        self.total = 0
        self.failed = 0