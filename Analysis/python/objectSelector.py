class ObjectSelector:
    def __init__(self, _year = "None" ):
        self.year = _year

class TauSelector(ObjectSelector):
    def __init__(self, _minPt = 20):
        self.minPt = _minPt

    def evalTau(self, tau):
        if tau.pt < self.minPt: return False
	# CHANGE: add basic tau selection criteria (eta, dz, decay mode, loosest discriminators against electrons/muons/jets)

        return True


class ElectronSelector(ObjectSelector):
    def __init__(self, _minPt = 10):
        self.minPt = _minPt

    def evalElectron(self, el):
        
        isEBEE = True if abs(el.eta)>1.4442 and abs(el.eta)<1.5660 else False
        
        if isEBEE: return False
        if el.pt < self.minPt: return False
        if abs(el.eta) > 2.4: return False
        if abs(el.dxy) > 0.1 or abs(el.dz) > 0.2: return False
        if not el.mvaIso_Fall17V2_WP90: return False

        return True
        
class MuonSelector(ObjectSelector):
    def __init__(self, minPt = 10):
        self.minPt = minPt

    def evalMuon(self, mu):
        if mu.pt < self.minPt: return False

	# CHANGE: add muon selection criteria (eta, dxy, dz, isolation, ID)

        return True
        
