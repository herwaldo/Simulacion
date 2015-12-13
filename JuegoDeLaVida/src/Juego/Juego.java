package Juego;

import java.awt.Color;
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.WindowConstants;

public class Juego {

    JFrame ventana;
    JPanel tablero;

    int tableroActual[][];
    int tableroSiguiente[][];
    int tableroAuxiliar[][];
    int alrededor[][];

    int filas = 0;
    int columnas = 0;

    JButton botones[][];

    public Juego(int filas, int columnas) {
        System.out.println("Bienvenido al Juego De La Vida");
        this.filas = filas;
        this.columnas = columnas;
    }

    public void IniciaJuego(int vida) throws InterruptedException {

        this.alrededor = new int[3][3];
        this.tableroActual = new int[filas][columnas];
        this.tableroSiguiente = new int[filas][columnas];
        this.tableroAuxiliar = new int[filas][columnas];

        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                this.tableroActual[i][j] = 0;
            }
        }

        crearVida(vida);

        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                botones[i][j].setBackground(Color.BLACK);
            }
        }

        do {
            for (int i = 0; i < filas - 2; i++) {
                for (int j = 0; j < columnas - 2; j++) {
                    this.alrededor[0][0] = tableroActual[i][j];
                    this.alrededor[0][1] = tableroActual[i][j + 1];
                    this.alrededor[0][2] = tableroActual[i][j + 2];
                    this.alrededor[1][0] = tableroActual[i + 1][j];
                    this.alrededor[1][1] = tableroActual[i + 1][j + 1];
                    this.alrededor[1][2] = tableroActual[i + 1][j + 2];
                    this.alrededor[2][0] = tableroActual[i + 2][j];
                    this.alrededor[2][1] = tableroActual[i + 2][j + 1];
                    this.alrededor[2][2] = tableroActual[i + 2][j + 2];

                    int contador = 0;

                    for (int k = 0; k < 3; k++) {
                        for (int l = 0; l < 3; l++) {
                            if (alrededor[k][l] == 1) {
                                contador++;
                            }
                        }
                    }

                    if (contador < 2 && alrededor[1][1] == 1) {
                        tableroSiguiente[i + 1][j + 1] = 0;
                    } else if (contador > 3 && alrededor[1][1] == 1) {
                        tableroSiguiente[i + 1][j + 1] = 0;
                    } else if (contador==3 && alrededor[1][1]==0){
                        tableroSiguiente[i+1][j+1]=1;
                    } else if (contador == 3 && alrededor[1][1]==1){
                        tableroSiguiente[i+1][j+1]=1;
                    }else if (contador==2){
                        tableroSiguiente[i+1][j+1]=tableroActual[i+1][j+1];
                    }
                }
            }

            tableroAuxiliar = tableroActual;
            tableroActual = tableroSiguiente;
            tableroSiguiente = tableroAuxiliar;

            Thread.sleep(500);

            coloresTablero(tableroSiguiente);
            for (int i = 0; i < filas; i++) {
                for (int j = 0; j < columnas; j++) {
                    this.tableroSiguiente[i][j] = 0;
                }
            }
        } while (true);

    }

    public void construirPanelVentana() {
        this.botones = new JButton[this.filas][this.columnas];
        tablero = new JPanel();
        tablero.setLayout(new GridLayout(this.filas, this.columnas));

        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                JButton boton = new JButton();
                String id = String.valueOf(i) + "-" + String.valueOf(j);
                boton.setName(id);
                boton.setSize(5, 5);
                boton.setToolTipText(id);

                botones[i][j] = boton;
            }
        }

        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                tablero.add(botones[i][j]);
            }
        }
    }

    public void constuirVentana() {
        ventana = new JFrame("El juego de la vida");
        ventana.setSize(800, 800);
        ventana.add(tablero);
        ventana.setVisible(true);
        ventana.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }

    public void coloresTablero(int[][] tabla) {
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if (tabla[i][j] == 1) {
                    botones[i][j].setBackground(Color.RED);
                }

                if (tabla[i][j] == 0) {
                    botones[i][j].setBackground(Color.BLACK);
                }

            }
        }
    }

    public void crearVida(int cantidad) {
        for (int i = 0; i < cantidad; i++) {
            int y = (int) Math.floor(Math.random() * (0 - filas + 1) + filas);
            int x = (int) Math.floor(Math.random() * (0 - columnas + 1) + columnas);

            tableroActual[y][x] = 1;
        }
    }
    
    public static void main(String args[]) throws InterruptedException{
        Juego begin = new Juego(Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero de Filas")), Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero de Columnas")));
        begin.construirPanelVentana();
        begin.constuirVentana();
        int vida = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero de bacterias"));
        begin.IniciaJuego(vida);
    }
}
