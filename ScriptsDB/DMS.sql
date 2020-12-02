USE Proyecto;

INSERT INTO User(var_userName,var_password, boo_type) VALUES 
    ("Gabriel","LanaRhoades", 0),
    ("Abner","EvaLovia", 1),
    ("David","MiaKalifa", 1),
    ("Daniela ","1234", 1)
;

INSERT INTO Binnacle(tex_action,id_user) VALUES 
    ("Circle",1),
    ("Cuadrado",2),
    ("Edito",3),
    ("Guardó ",1)
;

INSERT INTO Color(var_fillColor, var_penColor, id_user) VALUES 
    ("#000000","#c82a54",1),
    ("#ffffff","#ef280f",2),
    ("#109dfa","#23bac4",3),
    ("#02ac66","#ff689d",4)
;

INSERT INTO Paint(var_name,jso_data,id_user) VALUES 
    ("dibujox",'{"GraphicsCommands": {"Commands": [{"command": "GoTo", "x": -1.0, "y": 5.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -8.0, "y": 12.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -18.0, "y": 25.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -27.0, "y": 42.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -34.0, "y": 58.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -41.0, "y": 67.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -44.0, "y": 71.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -48.0, "y": 73.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -52.0, "y": 73.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -61.0, "y": 70.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -69.0, "y": 61.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -77.0, "y": 50.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -83.0, "y": 37.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -89.0, "y": 19.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -94.0, "y": 1.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -98.0, "y": -13.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -100.0, "y": -24.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -100.0, "y": -29.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -100.0, "y": -31.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -100.0, "y": -31.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -98.0, "y": -34.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -88.0, "y": -38.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -74.0, "y": -41.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -56.0, "y": -43.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -36.0, "y": -43.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -20.0, "y": -41.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": -7.0, "y": -38.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": 1.0, "y": -36.0, "width": 1.0, "color": "#000000"}, {"command": "GoTo", "x": 3.0, "y": -34.0, "width": 1.0, "color": "#000000"}]}}',1)
;