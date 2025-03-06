import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date

# Configuración de página
st.set_page_config(
    page_title="Reporte EEUU-LATAM | CEPAL Lab",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS personalizado
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Source+Sans+Pro:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Source Sans Pro', sans-serif;
        color: #333333;
    }
    
    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
        color: #052B5E;
    }
    
    h1 {
        font-size: 2.5rem;
        font-weight: 700;
        border-bottom: 1px solid #EEEEEE;
        padding-bottom: 1rem;
        margin-bottom: 2rem;
    }
    
    h2 {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 2rem;
    }
    
    h3 {
        font-size: 1.4rem;
        font-weight: 400;
        margin-top: 1.5rem;
    }
    
    .highlight {
        background-color: #F5F8FA;
        padding: 1.5rem;
        border-radius: 5px;
        border-left: 4px solid #0078D4;
        margin: 1rem 0;
    }
    
    .metric-container {
        background-color: white;
        padding: 1rem;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    .small-text {
        font-size: 0.8rem;
        color: #666666;
    }
    
    .divider {
        height: 1px;
        background-color: #EEEEEE;
        margin: 2rem 0;
    }
    
    /* Estilo para tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #F0F2F6;
        border-radius: 4px 4px 0px 0px;
        padding: 10px 16px;
        font-family: 'Source Sans Pro', sans-serif;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #0078D4;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

periodo = "Semana del 01 al 7 de marzo, 2025"
# Sidebar para navegación
st.sidebar.title("Contenido")
st.sidebar.markdown("### Reporte EEUU-LATAM")
st.sidebar.markdown(periodo)

pages = {
    "Resumen Ejecutivo": "Principales hallazgos de la semana",
    "1. Principales Temas": "Decisiones de EE.UU. con impacto en LATAM",
    "2. Detalle de Implicancias": "Comercio, inversión, migración y seguridad",
    "3. Detalle por Países": "Análisis por país y posibles impactos",
    "4. Áreas Críticas": "Variables para monitoreo futuro"
}

for page, description in pages.items():
    st.sidebar.markdown(f"[{page}](#{page.lower().replace(' ', '-').replace('.', '')})")
    st.sidebar.markdown(f"<span class='small-text'>{description}</span>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### Contacto")
st.sidebar.markdown("lab_cepal@un.org")
st.sidebar.markdown("Tel: +1 (xxx) xxx-xxxx")

# Encabezado
col1, col2 = st.columns([3, 1])
with col1:
    st.image("logo lab.png", width=200)
    st.title("Reporte Semanal EEUU - Latinoamérica")
    st.markdown(f"**{periodo}**")
#with col2:
    #st.image("logo lab.png", width=180)

st.markdown("---")

# Resumen ejecutivo
st.markdown("""
<div class="highlight">
<h3>Resumen Ejecutivo</h3>
<p>Esta semana, las decisiones de política comercial de Estados Unidos se han centrado en revisión de aranceles con impacto potencial en exportaciones latinoamericanas. Las inversiones en infraestructura energética y la nueva política migratoria podrían reconfigurar significativamente las relaciones con países clave como México, Brasil y Colombia.</p>
</div>
""", unsafe_allow_html=True)

###### SECCIÓN 1: PRINCIPALES TEMAS ######
st.header("1. Principales Temas")

# Crear datos de ejemplo para el gráfico de principales temas
temas_data = pd.DataFrame({
    'Tema': ['Revisión arancelaria', 'Política energética', 'Migración', 'Seguridad regional', 'Inversión tecnológica'],
    'Menciones': [78, 65, 52, 45, 32],
    'Impacto Potencial': [8.5, 7.9, 9.2, 6.8, 7.4]
})

col1, col2 = st.columns([2, 1])

with col1:
    # Gráfico de barras para temas principales
    fig = px.bar(
        temas_data, 
        x='Tema', 
        y='Menciones',
        color='Impacto Potencial',
        color_continuous_scale='Blues',
        text='Menciones',
        height=400
    )
    fig.update_layout(
        title='Principales temas de la semana',
        xaxis_title='',
        yaxis_title='Número de menciones',
        coloraxis_colorbar_title='Índice de<br>Impacto',
        plot_bgcolor='white',
        font=dict(family="Source Sans Pro"),
        margin=dict(t=50, b=0, l=0, r=0)
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Hallazgos clave")
    st.markdown("""
    📊 La **revisión arancelaria** domina la agenda con impacto directo en exportaciones de materias primas.
    
    🔋 La nueva **política energética** busca aumentar inversiones en energías renovables en LATAM.
    
    👥 El tema **migratorio** muestra el mayor índice de impacto potencial (9.2/10) con nuevas restricciones anunciadas.
    """)

# Detalles de los temas principales
st.markdown("""
#### Análisis de decisiones clave

El gobierno estadounidense anunció esta semana una revisión integral de su política arancelaria que podría beneficiar a exportadores de México y Brasil, mientras que impone nuevas restricciones a productos específicos de Colombia y Chile. El Departamento de Energía ha propuesto un fondo de $5 mil millones para inversiones en infraestructura energética limpia en Latinoamérica, con enfoque en Brasil, Colombia y Argentina.

La nueva política migratoria, aunque restrictiva en sus controles fronterizos, contempla programas de trabajadores temporales que podrían aliviar presiones en países como Guatemala y Honduras.
""")

###### SECCIÓN 2: DETALLE DE IMPLICANCIAS ######
st.header("2. Detalle de Implicancias")

# Crear datos simulados
comercio_data = {
    'Categoría': ['Materias primas', 'Manufacturas', 'Servicios', 'Energía', 'Agricultura'],
    'Cambio % Esperado': [3.5, -1.2, 0.8, 4.7, 2.1]
}

inversion_data = {
    'Sector': ['Tecnología', 'Energía verde', 'Infraestructura', 'Finanzas', 'Manufactura'],
    'Inversión (MM USD)': [850, 1200, 680, 520, 470],
    'Crecimiento Anual (%)': [12, 28, 5, 9, -3]
}

migracion_data = pd.DataFrame({
    'País': ['México', 'Guatemala', 'Honduras', 'El Salvador', 'Colombia', 'Venezuela'],
    'Remesas (MM USD)': [4200, 950, 720, 620, 350, 180],
    'Impacto Migratorio': [8, 9, 9, 7, 6, 10]  # Escala 1-10
})

seguridad_data = pd.DataFrame({
    'Área': ['Narcotráfico', 'Crimen organizado', 'Ciberseguridad', 'Terrorismo', 'Tráfico de personas'],
    'Índice de Cooperación': [7, 6, 8, 5, 7],  # Escala 1-10
    'Financiamiento US (MM USD)': [120, 80, 60, 30, 50]
})

# Crear tabs para cada categoría
tab1, tab2, tab3, tab4 = st.tabs(["Comercio", "Inversión", "Migración", "Seguridad"])

with tab1:
    st.subheader("Impacto Comercial")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        comercio_df = pd.DataFrame(comercio_data)
        fig = px.bar(
            comercio_df, 
            x='Categoría', 
            y='Cambio % Esperado',
            color='Cambio % Esperado',
            color_continuous_scale=['#D6324A', '#DFDFDF', '#0078D4'],
            text='Cambio % Esperado',
            height=350
        )
        fig.update_layout(
            title='Cambio porcentual esperado por categoría comercial',
            plot_bgcolor='white',
            yaxis_title='Cambio Esperado (%)',
            xaxis_title='',
            coloraxis_showscale=False,
            margin=dict(t=50, b=0, l=0, r=0)
        )
        fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        #### Análisis Comercial
        
        Las nuevas políticas arancelarias de EE.UU. beneficiarán principalmente al sector energético (+4.7%) y materias primas (+3.5%), mientras que el sector manufacturero podría experimentar una contracción (-1.2%).
        
        Los acuerdos bilaterales revisados con México y Brasil están generando nuevas oportunidades para exportadores agrícolas.
        """)

with tab2:
    st.subheader("Tendencias de Inversión")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        inversion_df = pd.DataFrame(inversion_data)
        fig = px.scatter(
            inversion_df,
            x='Sector',
            y='Crecimiento Anual (%)',
            size='Inversión (MM USD)',
            color='Crecimiento Anual (%)',
            color_continuous_scale='Blues',
            size_max=50,
            height=400
        )
        fig.update_layout(
            title='Inversión por sector y tasa de crecimiento',
            plot_bgcolor='white',
            yaxis_title='Crecimiento Anual (%)',
            xaxis_title='',
            margin=dict(t=50, b=0, l=0, r=0)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        #### Perspectivas de Inversión
        
        El sector de **energías renovables** lidera con un crecimiento anual del 28% y una inversión de $1,200 millones, impulsado por nuevas políticas de transición energética.
        
        La **inversión tecnológica** ($850M) continúa fuerte con un enfoque en digitalización y servicios financieros.
        
        La **manufactura** es el único sector que muestra contracción (-3%), afectado por tensiones comerciales y reestructuración de cadenas de suministro.
        """)

with tab3:
    st.subheader("Dinámica Migratoria")
    
    fig = px.scatter(
        migracion_data,
        x='País',
        y='Remesas (MM USD)',
        size='Impacto Migratorio',
        color='Impacto Migratorio',
        color_continuous_scale='Blues',
        size_max=50,
        height=400
    )
    fig.update_layout(
        title='Relación entre remesas e impacto de políticas migratorias',
        plot_bgcolor='white',
        yaxis_title='Remesas (Millones USD)',
        xaxis_title='',
        coloraxis_colorbar_title='Índice de<br>Impacto',
        margin=dict(t=50, b=0, l=0, r=0)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Hallazgos Clave
        
        • Venezuela muestra el mayor índice de impacto potencial (10/10) debido a las políticas de protección temporal.
        
        • México recibe el mayor volumen de remesas ($4,200M), con alta sensibilidad a cambios regulatorios.
        
        • Guatemala y Honduras (9/10) enfrentan desafíos significativos debido a su dependencia económica de remesas y flujo migratorio.
        """)
    
    with col2:
        st.markdown("""
        #### Perspectivas
        
        La nueva política migratoria de EE.UU. incluirá un programa de **trabajadores temporales agrícolas** que podría beneficiar a países centroamericanos.
        
        Se estima un **aumento del 7%** en el flujo de remesas para el próximo trimestre, pero con mayor escrutinio bancario.
        
        Los acuerdos bilaterales de seguridad fronteriza requerirán mayor cooperación regional con incentivos económicos.
        """)

with tab4:
    st.subheader("Cooperación en Seguridad")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = px.bar(
            seguridad_data,
            x='Área',
            y='Financiamiento US (MM USD)',
            color='Índice de Cooperación',
            color_continuous_scale='Blues',
            text='Financiamiento US (MM USD)',
            height=400
        )
        fig.update_layout(
            title='Financiamiento e índice de cooperación por área de seguridad',
            plot_bgcolor='white',
            yaxis_title='Financiamiento (Millones USD)',
            xaxis_title='',
            coloraxis_colorbar_title='Índice de<br>Cooperación',
            margin=dict(t=50, b=0, l=0, r=0)
        )
        fig.update_traces(texttemplate='$%{text}M', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        #### Prioridades de Seguridad
        
        • La lucha contra el **narcotráfico** continúa siendo la principal área de financiamiento ($120M) con alto índice de cooperación.
        
        • La **ciberseguridad** muestra el mayor nivel de cooperación (8/10) con programas de entrenamiento y equipamiento.
        
        • El **terrorismo** muestra el menor índice de cooperación (5/10) pero podría incrementarse debido a preocupaciones emergentes.
        """)

###### SECCIÓN 3: DETALLE POR PAÍSES ######
st.header("3. Detalle por Países")

# Datos de ejemplo para países
paises_data = pd.DataFrame({
    'País': ['México', 'Brasil', 'Colombia', 'Chile', 'Argentina', 'Perú'],
    'Menciones': [105, 87, 62, 45, 43, 35],
    'Áreas Clave': ['Comercio, Migración, Seguridad', 'Inversión, Energía, Comercio', 
                    'Seguridad, Energía', 'Comercio, Inversión', 'Finanzas, Comercio', 'Minería, Inversión'],
    'Impacto': [8.5, 7.9, 7.2, 6.5, 6.3, 5.8],
    'Tendencia': ['↑', '↑', '→', '↓', '↓', '→']
})

# Mapa interactivo de Latinoamérica
st.subheader("Impacto por país")

# Crear un mapa de calor para visualizar impacto por país
impact_map = pd.DataFrame({
    'País': paises_data['País'],
    'Impacto': paises_data['Impacto']
})

fig = px.choropleth(
    impact_map,
    locations='País',
    locationmode='country names',
    color='Impacto',
    color_continuous_scale='Blues',
    scope="south america",
    height=500,
    title='Mapa de impacto potencial en Latinoamérica'
)

# Ajusta el mapa para incluir a México
fig.update_geos(
    lataxis_range=[-60, 35],
    lonaxis_range=[-120, -30]
)

fig.update_layout(
    margin=dict(t=50, b=0, l=0, r=0),
    coloraxis_colorbar_title='Índice de<br>Impacto'
)

st.plotly_chart(fig, use_container_width=True)

# Tabla de países
st.subheader("Países mencionados esta semana")
st.dataframe(
    paises_data.style.background_gradient(subset=['Impacto'], cmap='Blues')
    .format({'Impacto': '{:.1f}/10'})
    .set_properties(**{'text-align': 'left'})
    .hide(axis='index'),
    height=300
)

# Detalle de países seleccionados
selected_country = st.selectbox("Seleccione un país para más detalles:", paises_data['País'])

# Datos específicos por país
country_data = {
    'México': {
        'overview': """
        **México** enfrenta importantes desafíos y oportunidades debido a su proximidad y estrecha relación con EE.UU. 
        La revisión del T-MEC y las nuevas políticas migratorias tendrán un impacto directo en su economía.
        """,
        'key_areas': ['Comercio: Revisión arancelaria automotriz', 'Migración: Controles fronterizos reforzados', 
                     'Inversión: Nearshoring en manufactura'],
        'economic_impact': [8.7, 9.2, 7.8, 6.5],  # Comercio, Inversión, Migración, Seguridad
        'economic_categories': ['Comercio', 'Inversión', 'Migración', 'Seguridad']
    },
    'Brasil': {
        'overview': """
        **Brasil** se posiciona como receptor principal de nuevas inversiones en energía renovable y tecnología.
        Las relaciones bilaterales muestran mejoría con nuevos acuerdos comerciales en discusión.
        """,
        'key_areas': ['Energía: Inversiones en renovables', 'Comercio: Exportaciones agrícolas', 
                     'Tecnología: Cooperación en semiconductores'],
        'economic_impact': [7.5, 8.9, 4.2, 6.1],
        'economic_categories': ['Comercio', 'Inversión', 'Migración', 'Seguridad']
    },
    'Colombia': {
        'overview': """
        **Colombia** mantiene su posición como aliado estratégico en seguridad, con nuevos programas de cooperación.
        Las inversiones en transición energética podrían transformar su matriz productiva.
        """,
        'key_areas': ['Seguridad: Programas antinarcóticos', 'Energía: Transición a renovables', 
                     'Migración: Políticas hacia venezolanos'],
        'economic_impact': [6.2, 7.8, 6.9, 9.1],
        'economic_categories': ['Comercio', 'Inversión', 'Migración', 'Seguridad']
    },
    'Chile': {
        'overview': """
        **Chile** enfrenta desafíos con las nuevas políticas comerciales, especialmente en minería y agricultura.
        Las inversiones tecnológicas muestran señales positivas en un contexto de incertidumbre política.
        """,
        'key_areas': ['Comercio: Aranceles a minerales críticos', 'Inversión: Tecnologías verdes', 
                     'Finanzas: Acuerdos de cooperación'],
        'economic_impact': [7.8, 6.5, 3.2, 5.4],
        'economic_categories': ['Comercio', 'Inversión', 'Migración', 'Seguridad']
    },
    'Argentina': {
        'overview': """
        **Argentina** busca estabilizar sus relaciones económicas en un contexto de volatilidad financiera.
        Los nuevos acuerdos de deuda y los programas agrícolas podrían ofrecer oportunidades de recuperación.
        """,
        'key_areas': ['Finanzas: Restructuración de deuda', 'Comercio: Exportaciones agrícolas', 
                     'Energía: Desarrollo de Vaca Muerta'],
        'economic_impact': [6.8, 5.9, 4.1, 4.7],
        'economic_categories': ['Comercio', 'Inversión', 'Migración', 'Seguridad']
    },
    'Perú': {
        'overview': """
        **Perú** mantiene un perfil moderado en las relaciones bilaterales, con enfoque en minería y comercio.
        La estabilidad política sigue siendo un factor determinante para futuras inversiones estadounidenses.
        """,
        'key_areas': ['Minería: Inversiones en cobre y litio', 'Comercio: TLC en revisión', 
                     'Seguridad: Programas antinarcóticos'],
        'economic_impact': [6.2, 5.7, 3.9, 6.8],
        'economic_categories': ['Comercio', 'Inversión', 'Migración', 'Seguridad']
    }
}

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(country_data[selected_country]['overview'])
    
    # Crear gráfico de radar para dimensiones de impacto
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=country_data[selected_country]['economic_impact'],
        theta=country_data[selected_country]['economic_categories'],
        fill='toself',
        name='Impacto',
        line_color='#0078D4'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )
        ),
        title=f"Dimensiones de impacto para {selected_country}",
        height=400,
        margin=dict(t=50, b=0, l=0, r=0)
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("### Áreas clave de atención")
    for area in country_data[selected_country]['key_areas']:
        st.markdown(f"• {area}")
    
    st.markdown("### Recomendaciones")
    st.markdown(f"""
    1. **Monitorear** cambios en política comercial de EE.UU.
    2. **Preparar** respuestas a escenarios de mayor restricción migratoria.
    3. **Identificar** oportunidades en nuevos programas de inversión energética.
    """)

###### SECCIÓN 4: ÁREAS CRÍTICAS ######
st.header("4. Áreas Críticas para Monitoreo")

# Datos para áreas críticas
areas_criticas = pd.DataFrame({
    'Área': ['Tasas de interés FED', 'Precios de commodities', 'Tensiones comerciales China-EEUU', 
             'Políticas migratorias', 'Restricciones ESG', 'Estímulos fiscales'],
    'Indicador Actual': [5.25, 102.3, 68, 45, 82, 38],
    'Tendencia': ['↑', '→', '↑', '↑', '↑', '↓'],
    'Impacto LATAM': [9.2, 8.7, 8.5, 7.8, 6.9, 7.2],
    'Categoría': ['Financiero', 'Económico', 'Comercial', 'Social', 'Regulatorio', 'Económico']
})

col1, col2 = st.columns([3, 1])

with col1:
    # Gráfico de burbujas para áreas críticas
    fig = px.scatter(
        areas_criticas,
        x='Área',
        y='Impacto LATAM',
        size='Indicador Actual',
        color='Categoría',
        color_discrete_sequence=px.colors.qualitative.Bold,
        text='Tendencia',
        hover_name='Área',
        size_max=60,
        height=450
    )
    fig.update_layout(
        title='Variables críticas para monitoreo económico',
        plot_bgcolor='white',
        yaxis_title='Índice de Impacto LATAM',
        xaxis_title='',
        margin=dict(t=50, b=0, l=0, r=0)
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Próximos indicadores a vigilar")
    st.markdown("""
    📅 **25 mayo**: Reunión FED - Decisión de tasas de interés
    
    📅 **1 junio**: Publicación de datos de empleo EE.UU.
    
    📅 **10 junio**: Implementación de nuevas regulaciones comerciales
    
    📅 **15 junio**: Decisión sobre subsidios agrícolas
    """)

# Añadir análisis final de áreas críticas
st.markdown("""
#### Implicaciones para proyecciones económicas

El monitoreo de estas variables críticas sugiere que la región latinoamericana enfrentará un entorno económico más restrictivo en los próximos meses. Las **tasas de interés de la FED** muestran la tendencia alcista con mayor impacto potencial (9.2/10), lo que podría generar presiones adicionales sobre los tipos de cambio y condiciones de financiamiento regional.

La evolución de los **precios de commodities** seguirá siendo determinante para los exportadores de materias primas, mientras que las **tensiones comerciales entre EE.UU. y China** podrían crear oportunidades de diversificación para países como México y Brasil.

Las **políticas migratorias** representan un factor de riesgo significativo para economías dependientes de remesas, particularmente en Centroamérica, donde podrían afectar hasta un 20% del PIB de algunos países.
""")

# Pie de página
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown('<p class="small-text">Reporte preparado por CEPAL Lab para el Trade Emergency Team</p>', unsafe_allow_html=True)
with col2:
    st.markdown('<p class="small-text">Datos actualizados al 6 de marzo, 2025</p>', unsafe_allow_html=True)
with col3:
    st.markdown('<p class="small-text">© Cepal Lab - Versión de prueba - contenido ficticio</p>', unsafe_allow_html=True)
