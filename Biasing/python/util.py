
from HPS.SimCore import simcfg

class StepPrinter(simcfg.UserAction):
  """Print each step of the input track ID
    The default track ID is 1 (the primary particle).
    Parameters
    ----------
    track_id : int, optional
        Geant4 track ID to print each step of
  """

  def __init__(self,track_id=1) :
    super().__init__('print_steps_%s'%track_id,'biasing::StepPrinter')

    self.track_id = track_id
