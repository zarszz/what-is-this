class Error(Exception):
  """base error exception"""
  pass

class NameHasAvaible(Error):
  """Operation Error : Name has avaible in database"""