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

# === Program Utama ===

def main():
    screen = turtle.Screen()
    screen.title("Tugas Geometri Dasar - Gitar Akustik")
    screen.bgcolor("#E8F0F2")
    screen.tracer(1)
    t = turtle.Turtle()
    t.speed("fast")
    
    t.hideturtle()
    t.pensize(2)

    CX = 0
    BODY_Y = -50

    # 1. ELIPS - Pembuatan Badan Bawah Gitar (Lower Bout)
    draw_ellipse(t, CX, BODY_Y - 90, 100, 100, "#C88A4A", "#5A3010")

    # 2. LINGKARAN - Pembuatan Badan Atas Gitar (Upper Bout)
    draw_circle(t, CX, BODY_Y + 40, 75, "#C88A4A", "#5A3010")

    # Menutupi garis potongan di tengah gabungan bangun ruang
    draw_ellipse(t, CX, BODY_Y - 90, 98, 98, "#C88A4A", "#C88A4A")
    draw_circle(t, CX, BODY_Y + 40, 73, "#C88A4A", "#C88A4A")
    # LINGKARAN - Pembuatan Lubang Suara (Sound Hole)
    hole_y = BODY_Y + 20
    draw_circle(t, CX, hole_y, 32, "#E0B050", "#8A5A20")
    draw_circle(t, CX, hole_y, 27, "#C88A4A", "#8A5A20")
    draw_circle(t, CX, hole_y, 22, "#201005", "black")

    # 3. TRAPESIUM - Pembuatan Pinggiran Bridge (Penahan Senar)
    bridge_y = BODY_Y - 110
    bridge_points = [
        (CX - 40, bridge_y - 10),
        (CX + 40, bridge_y - 10),
        (CX + 30, bridge_y + 10),
        (CX - 30, bridge_y + 10)
    ]
    draw_polygon(t, bridge_points, "#402010", "black")
    draw_line(t, CX - 25, bridge_y + 5, CX + 25, bridge_y + 5, "white", 3)
    # 4. POLIGON (PERSEGI PANJANG) - Pembuatan Leher Gitar (Neck)
    neck_bottom = hole_y + 27
    neck_top = neck_bottom + 240
    neck_w = 16

    neck_pts = [
        (CX - neck_w, neck_bottom),
        (CX - neck_w, neck_top),
        (CX + neck_w, neck_top),
        (CX + neck_w, neck_bottom)
    ]
    draw_polygon(t, neck_pts, "#6A3A1A", "black")
    
    for i in range(1, 15): 
        y_fret = neck_bottom + (i * 16)
        draw_line(t, CX - neck_w, y_fret, CX + neck_w, y_fret, "silver", 2)
    # 5. JAJARAN GENJANG - Kepala Gitar (Headstock)
    head_bottom = neck_top
    head_top = neck_top + 60
    head_w = 25
    slant = 10

    head_pts = [
        (CX - head_w, head_bottom),
        (CX - head_w + slant, head_top),
        (CX + head_w + slant, head_top),
        (CX + head_w, head_bottom)
    ]
    draw_polygon(t, head_pts, "#804020", "black")

    # 6. Tuning Pegs
    peg_y_list = [head_bottom + 15, head_bottom + 35, head_bottom + 55]
    for py in peg_y_list:
        s_offset = slant * ((py - head_bottom) / 60)
        draw_circle(t, CX - head_w - 10 + s_offset, py, 6, "silver", "black")
        draw_line(t, CX - head_w - 4 + s_offset, py, CX - head_w + 3 + s_offset, py, "gray", 3)
        draw_circle(t, CX + head_w + 10 + s_offset, py, 6, "silver", "black")
        draw_line(t, CX + head_w + 4 + s_offset, py, CX + head_w - 3 + s_offset, py, "gray", 3)
    # 7. Penarikan Garis Lurus - Representasi Senar
    for i in range(6):
        x_offset = -12 + (i * 4.8)
        x_bawah = CX + x_offset * 1.5 
        y_bawah = bridge_y + 5
        x_atas = CX + x_offset
        y_atas = neck_top
        draw_line(t, x_bawah, y_bawah, x_atas, y_atas, "#E0E0E0", 1)

    def save_and_close(x, y):
        cv = turtle.getcanvas()
        cv.postscript(file="gitar.eps")
        screen.bye()

    screen.update()
    screen.onscreenclick(save_and_close)
    turtle.done()

if __name__ == "__main__":
    main()
