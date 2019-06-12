import ghpythonlib.components as ghc
import ghpythonlib.parallel as ghp

#divide circle curves into pnts
indivpoints = {}
for circle in circles:
    points = ghc.DivideCurve(circle, splits, False)[0]
    for num in range(0, splits):
        indivpoints.update({num:[points[num]]}) if num not in indivpoints.keys() else indivpoints[num].append(points[num])

#create polylines from points at index between circles
polylines = [ghc.PolyLine(indivpoints[key], False) for key in indivpoints.keys()] 
polylines.append(polylines[0])#to allow a full loop

#create ruled surfaces between polylines
loftsdata = [[polylines[loft],polylines[loft+1]] for loft in range(0, splits)]

#running ruled surfaces in parallel compute
lofts = ghc.CapHoles(ghc.BrepJoin(ghp.run(lambda x: ghc.RuledSurface(x[0], x[1]), loftsdata, True))[0])