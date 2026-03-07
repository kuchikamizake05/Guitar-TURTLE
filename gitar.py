import turtle
import math


# ===========================
# BLOCK FUNGSI GEOMETRI DASAR
# ===========================
# Berisi fungsi-fungsi custom untuk memudahkan penggambaran bentuk dasar

def draw_polygon(t, points, color_fill, color_pen="black"):
    # Fungsi untuk menggambar poligon bebas berdasarkan list koordinat (x,y)
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.color(color_pen, color_fill)
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0]) # balik ke titik awal biar ketutup
    t.end_fill()


def draw_circle(t, x, y, radius, color_fill, color_pen="black"):
    # Fungsi dasar menggambar lingkaran
    t.penup()
    t.goto(x, y - radius) # Offset Y agar titik tengah lingkaran pas di (x,y)
    t.pendown()
    t.color(color_pen, color_fill)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_ellipse(t, cx, cy, a, b, color_fill, color_pen="black"):
    """Menggambar elips menggunakan rumus parametrik (x = a*cos, y = b*sin)"""
    t.penup()
    t.color(color_pen, color_fill)
    t.goto(cx + a, cy)
    t.pendown()
    t.begin_fill()
    for i in range(0, 361, 5): # Menggunakan step 5 derajat untuk optimasi rendering
        rad = math.radians(i)
        t.goto(cx + a * math.cos(rad), cy + b * math.sin(rad))
    t.end_fill()


def draw_line(t, x1, y1, x2, y2, color="black", pen_size=1):
    # fungsi buat tarik garis lurus doang sih ini
    t.pensize(pen_size)
    t.penup()
    t.color(color)
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.pensize(2)  # balikin ukuran pena ke defaultnya (2)
