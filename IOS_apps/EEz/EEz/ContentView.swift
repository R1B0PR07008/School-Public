//
//  ContentView.swift
//  EEz
//
//  Created by Matias Riboldi on 26/10/2024.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        
        NavigationView() {
            List {
                NavigationLink("Rojo") {
                    Rojo()
                }
                NavigationLink("Verde") {
                    Verde()
                }
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
