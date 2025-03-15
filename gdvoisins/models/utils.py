

def notanytest(val):
  return any(
      [
          val is None,
          val == "",
          val == "<p></p>",
      ]
  )