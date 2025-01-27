from trace_collector import events

class MemoryLayoutView(object):
  def __init__(self):
    self.snapshots = []
    self.current = None

  def update(self, entry, session):
    if entry[0] == events.MEMORY_LAYOUT:
      self.current = MemoryLayoutData(entry[1], entry[2])
      self.snapshots.append(self.current)

class MemoryLayoutData(object):
  __slots__ = [
    'timestamp', 'static_base', 'static_top',
    'stack_base', 'stack_top', 'stack_max',
    'dynamic_base', 'dynamic_top', 'total_memory'
  ]
  def __init__(self, timestamp, data):
    self.timestamp = timestamp
    self.static_base = data['static_base'] if 'static_base' in data.keys() else 0
    self.static_top = data['static_top'] if 'static_top' in data.keys() else 0
    self.stack_base = data['stack_base'] if 'stack_base' in data.keys() else 0
    self.stack_top = data['stack_top'] if 'stack_top' in data.keys() else 0
    self.stack_max = data['stack_max'] if 'stack_max' in data.keys() else 0
    self.dynamic_base = data['dynamic_base'] if 'dynamic_base' in data.keys() else 0
    self.dynamic_top = data['dynamic_top'] if 'dynamic_top' in data.keys() else 0
    self.total_memory = data['total_memory'] if 'total_memory' in data.keys() else 0
