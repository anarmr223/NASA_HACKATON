// Instala: npm install turf @turf/turf

import * as turf from '@turf/turf';

class ImpactDamageAnalyzer {
    constructor() {
        this.countriesData = null;
    }

    // Cargar datos geoespaciales de países
    async loadCountriesData() {
        try {
            const response = await fetch('https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson');
            this.countriesData = await response.json();
        } catch (error) {
            console.error('Error loading countries data:', error);
        }
    }

    // Analizar impacto
    analyzeImpact(impactLat, impactLon, radiusKm) {
        if (!this.countriesData) {
            throw new Error('Countries data not loaded. Call loadCountriesData() first.');
        }

        // Crear punto de impacto
        const impactPoint = turf.point([impactLon, impactLat]);
        
        // Crear círculo de daño
        const damageRadius = turf.circle(impactPoint, radiusKm, {
            steps: 64,
            units: 'kilometers'
        });

        const affectedCountries = [];

        // Verificar cada país
        this.countriesData.features.forEach(country => {
            const countryGeometry = country.geometry;
            
            // Verificar intersección
            const intersects = turf.booleanIntersects(damageRadius, countryGeometry);
            
            if (intersects) {
                // Calcular porcentaje de afectación
                const intersection = turf.intersect(damageRadius, countryGeometry);
                let affectedPercentage = 0;
                
                if (intersection) {
                    const countryArea = turf.area(countryGeometry);
                    const affectedArea = turf.area(intersection);
                    affectedPercentage = (affectedArea / countryArea) * 100;
                }

                affectedCountries.push({
                    name: country.properties.NAME || country.properties.ADMIN,
                    isoCode: country.properties.ISO_A3 || country.properties.ADM0_A3,
                    affectedPercentage: Math.min(affectedPercentage, 100),
                    severity: this.calculateSeverity(affectedPercentage)
                });
            }
        });

        return affectedCountries.sort((a, b) => b.affectedPercentage - a.affectedPercentage);
    }

    calculateSeverity(percentage) {
        if (percentage >= 80) return 'CRITICAL';
        if (percentage >= 50) return 'HIGH';
        if (percentage >= 20) return 'MEDIUM';
        if (percentage >= 5) return 'LOW';
        return 'MINIMAL';
    }
}

// Uso del sistema
async function main() {
    const analyzer = new ImpactDamageAnalyzer();
    await analyzer.loadCountriesData();
    
    // Ejemplo: Impacto en Europa Central
    const results = analyzer.analyzeImpact(48.8566, 2.3522, 500); // París, 500km radio
    
    console.log('Países afectados:');
    results.forEach(country => {
        console.log(`${country.name}: ${country.affectedPercentage.toFixed(2)}% - ${country.severity}`);
    });
    
    return results;
}