import pandas as pd
from dataclasses import dataclass
from typing import Dict, List

# -------------------- KPI DATA --------------------
@dataclass
class KPIMetrics:
    average_price: float = 950
    average_discount: float = 40
    average_rating: float = 3.8

    def __post_init__(self):
        self.effective_price = self.average_price * (1 - self.average_discount / 100)


kpis = KPIMetrics()

print("=" * 70)
print("E-COMMERCE KPI ANALYSIS & BUSINESS INSIGHTS")
print("=" * 70)


# -------------------- ANALYZER CLASS --------------------
class KPIAnalyzer:
    def __init__(self, kpis: KPIMetrics):
        self.kpis = kpis

    # ---------- PRICING ----------
    def analyze_pricing_strategy(self) -> Dict:
        print("\n📊 PRICING STRATEGY ANALYSIS")
        print("-" * 70)

        revenue_loss = self.kpis.average_price - self.kpis.effective_price

        print(f"✓ Original Price        : ${self.kpis.average_price:.2f}")
        print(f"✓ Average Discount      : {self.kpis.average_discount}%")
        print(f"✓ Effective Price       : ${self.kpis.effective_price:.2f}")
        print(f"✓ Revenue Loss / Unit   : ${revenue_loss:.2f}")

        if self.kpis.average_discount >= 35:
            print("\n⚠️ CRITICAL INSIGHT:")
            print("• Heavy discounting (40%) risks margin erosion")
            print("• Indicates pricing or product-value issues")

        return {
            "original_price": self.kpis.average_price,
            "discount": self.kpis.average_discount,
            "effective_price": self.kpis.effective_price,
            "revenue_loss": revenue_loss,
        }

    # ---------- CUSTOMER SATISFACTION ----------
    def analyze_customer_satisfaction(self) -> Dict:
        print("\n⭐ CUSTOMER SATISFACTION ANALYSIS")
        print("-" * 70)

        satisfaction_pct = (self.kpis.average_rating / 5) * 100
        sentiment = self._get_rating_sentiment(self.kpis.average_rating)

        print(f"✓ Average Rating        : {self.kpis.average_rating}/5")
        print(f"✓ Satisfaction Level    : {satisfaction_pct:.1f}%")
        print(f"✓ Sentiment             : {sentiment}")

        if self.kpis.average_rating < 4.0:
            print("\n⚠️ BELOW-AVERAGE EXPERIENCE:")
            print("• Discounts are not compensating for quality/service issues")

        return {
            "rating": self.kpis.average_rating,
            "satisfaction_pct": satisfaction_pct,
            "sentiment": sentiment,
        }

    # ---------- DISCOUNT vs RATING ----------
    def analyze_discount_rating_correlation(self) -> Dict:
        print("\n🔗 DISCOUNT vs RATING ANALYSIS")
        print("-" * 70)

        risk_level = "LOW"
        issues = []

        if self.kpis.average_discount > 35 and self.kpis.average_rating < 4.0:
            risk_level = "CRITICAL"
            issues.append("High discount NOT improving satisfaction")
            issues.append("Root cause likely quality or fulfillment")

        print(f"✓ Discount : {self.kpis.average_discount}%")
        print(f"✓ Rating   : {self.kpis.average_rating}")
        print(f"✓ Risk     : {risk_level}")

        for issue in issues:
            print(f"  • {issue}")

        return {
            "discount": self.kpis.average_discount,
            "rating": self.kpis.average_rating,
            "risk_level": risk_level,
            "issues": issues,
        }

    # ---------- RECOMMENDATIONS ----------
    def generate_business_recommendations(self) -> List[str]:
        print("\n💡 STRATEGIC RECOMMENDATIONS")
        print("-" * 70)

        margin_loss = self.kpis.average_price * self.kpis.average_discount / 100

        recs = [
            "Reduce blanket discount from 40% → 25–30%",
            "Improve product quality & delivery to raise rating ≥ 4.3",
            f"Recover margin loss of ${margin_loss:.2f} per unit",
            "Introduce segment-based and loyalty discounts",
        ]

        for i, rec in enumerate(recs, 1):
            print(f"{i}. {rec}")

        return recs

    # ---------- DASHBOARD ----------
    def create_summary_dashboard(self):
        print("\n" + "=" * 70)
        print("KPI DASHBOARD SUMMARY")
        print("=" * 70)

        df = pd.DataFrame({
            "Metric": ["Avg Price", "Discount", "Effective Price", "Rating"],
            "Value": [
                f"${self.kpis.average_price:.2f}",
                f"{self.kpis.average_discount}%",
                f"${self.kpis.effective_price:.2f}",
                f"{self.kpis.average_rating}★",
            ],
            "Status": ["⚠️", "🔴", "⚠️", "🟠"]
        })

        print(df.to_string(index=False))

        print("\n📈 PROFIT SCENARIOS (1000 Units)")
        print("-" * 70)

        units = 1000
        current = self.kpis.effective_price * units
        scenario_30 = self.kpis.average_price * 0.70 * units
        scenario_30_vol = scenario_30 * 1.15
        scenario_25_rating = self.kpis.average_price * 0.75 * units * 1.1

        print(f"Current (40%)                 : ${current:,.0f}")
        print(f"30% Discount                  : ${scenario_30:,.0f}")
        print(f"30% + 15% Volume              : ${scenario_30_vol:,.0f}")
        print(f"25% + Better Rating           : ${scenario_25_rating:,.0f}")

    # ---------- HELPER ----------
    def _get_rating_sentiment(self, rating: float) -> str:
        if rating >= 4.5:
            return "Excellent 🟢"
        elif rating >= 4.0:
            return "Good 🟡"
        elif rating >= 3.0:
            return "Average 🟠"
        return "Poor 🔴"


# -------------------- RUN ANALYSIS --------------------
analyzer = KPIAnalyzer(kpis)
analyzer.analyze_pricing_strategy()
analyzer.analyze_customer_satisfaction()
analyzer.analyze_discount_rating_correlation()
analyzer.generate_business_recommendations()
analyzer.create_summary_dashboard()