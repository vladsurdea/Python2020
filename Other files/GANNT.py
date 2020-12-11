import plotly.figure_factory as ff

df = [dict(Task="A1.Falling Skies", Start='2020-10-01', Finish='2020-11-15', Resource="Mitchell"),
      dict(Task="A2.Trivia", Start='2020-10-01', Finish='2020-11-01', Resource="Sofia"),
      dict(Task="A3.Text-Based Adventure", Start='2020-10-10', Finish='2020-11-30', Resource="Vlad"),
      dict(Task="A4.New-game", Start='2020-11-01', Finish='2020-11-30', Resource="Team Effort"),
      dict(Task="B.Visual Design", Start='2020-10-30', Finish='2020-11-15', Resource="Vlad"),
      dict(Task="C.Game Design", Start='2020-10-01', Finish='2020-10-30', Resource="Mitchell"),
      dict(Task="D.UI Design", Start='2020-11-25', Finish='2020-10-30', Resource="Sofia"),
      dict(Task="E.Final Report Writing and Final Pitch", Start='2020-11-15', Finish='2020-11-30', Resource="Team Effort"),
      dict(Task="F.Mid-term Report Writing", Start='2020-10-15', Finish='2020-10-25', Resource="Team Effort"),
      dict(Task="G.Initial Pitch", Start='2020-10-01', Finish='2020-10-07', Resource="Team Effort")]

fig = ff.create_gantt(df,index_col='Resource',show_colorbar=True,showgrid_x=True,showgrid_y=True,title="Fire, Fire Walk with ME — GANTT",show_hover_fill=True)
fig.show()