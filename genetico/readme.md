https://www.pybonacci.org/2012/04/13/dibujando-lineas-de-nivel-en-python-con-matplotlib/

https://www.python-course.eu/matplotlib_contour_plot.php

https://plot.ly/python/dot-plots/


Agradecimento ao mito do rodrigo borges pela parte do codigo abaixo: 
-sem ele não seria possível fazer as plotagens


import plotly.plotly as py
import plotly.offline as pyo
import plotly.graph_objs as go
pyo.init_notebook_mode()


def f(x):
  
  squared = x[0]*x[0] + x[1]*x[1]
  sin = np.sin(np.sqrt(squared))
  denominator = 1 + 0.001*squared
  
  return 0.5 - (sin*sin - 0.5) / (denominator*denominator)


def calculate_z_matrix(X, Y, f):
  
  Z = np.zeros((len(X),len(Y)))
  for i, x in enumerate(X):
    for j, y in enumerate(Y):
      Z[i][j] = f([x,y])
  
  return Z


def create_contour_tracer(X, Y, f):
  
  Z = calculate_z_matrix(X, Y, f)
  
  contour_tracer = dict(
    type='contour',
    x=X, y=Y,
    z=Z,
    colorscale='Reds',
    showlegend=False)
  
  return contour_tracer


X_range = [-10, 10]
Y_range = [-10, 10]

X = np.linspace(*X_range, 101)
Y = np.linspace(*Y_range, 101)

tracers = []

contour_tracer = create_contour_tracer(X, Y, f)
tracers.append(contour_tracer)

figure = go.Figure(data=tracers)
pyo.iplot(figure)
