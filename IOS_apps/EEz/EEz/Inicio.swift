//
//  Inicio.swift
//  EEz
//
//  Created by Matias Riboldi on 26/10/2024.
//

import SwiftUI

struct Inicio: View {
    var body: some View {
        TabView {
            ContentView().tabItem {
                Label("ContentView", systemImage: "contextualmenu.and.cursorarrow")
            }
            
            Dash().tabItem {
                Label("Dash", systemImage: "helm")
            }
            
            Rojo() .tabItem{
                Label("Rojo", systemImage: "globe")
                
            }
            Verde() .tabItem {
                Label("verde", systemImage: "box.truck.fill")
            }
            
        }
        
    }
}

struct Inicio_Previews: PreviewProvider {
    static var previews: some View {
        Inicio()
    }
}
